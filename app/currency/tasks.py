import requests

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from currency.utils import to_decimal
from currency import model_choices as mch
from currency import consts


@shared_task
def slow_func():
    from time import sleep
    print('START')
    sleep(10)
    print('END')
    # send to broker
    return


@shared_task(autoretry_for=(OSError,), retry_kwargs={'max_retries': 5})
def send_contact_us_email(subject, from_email):
    email_subject = 'ContactUs From Currency Project'
    body = f'''
    Subject From Client: {subject}
    Email: {from_email}
    Wants to contact
    '''

    from time import sleep
    sleep(3)
    # print('send_contact_us_email')
    # raise OSError
    send_mail(
        email_subject,
        body,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )

    # ContactUs.objects.create()


@shared_task
def parse_privatbank():
    from currency.models import Rate, Source

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'

    response = requests.get(url)
    response.raise_for_status()  # raise error if not ok

    response_data = response.json()

    currency_type_mapper = {
        'UAH': mch.CurrencyType.CURRENCY_TYPE_UAH,
        'USD': mch.CurrencyType.CURRENCY_TYPE_USD,
        'EUR': mch.CurrencyType.CURRENCY_TYPE_EUR,
        'BTC': mch.CurrencyType.CURRENCY_TYPE_BTC,
    }

    # try:
    #     source = Source.objects.get(name=source_name)
    # except Source.DoesNotExist:
    #     source = Source.objects.create(name=source_name, url=url)

    # source, created = Source.objects.get_or_create(name=source_name, defaults={'url': url})
    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_PRIVATBANK,
        defaults={'url': url, 'name': 'PrivatBank'},
    )[0]

    for rate_data in response_data:
        currency_type = rate_data['ccy']
        base_currency_type = rate_data['base_ccy']

        # skip unsupported currencies
        if currency_type not in currency_type_mapper or \
                base_currency_type not in currency_type_mapper:
            continue

        # convert privatbank currency into our custom currency type
        currency_type = currency_type_mapper[rate_data['ccy']]
        base_currency_type = currency_type_mapper[rate_data['base_ccy']]

        buy = to_decimal(rate_data['buy'])
        sale = to_decimal(rate_data['sale'])

        try:
            latest_rate = Rate.objects.filter(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                source=source,
            ).latest('created')
        except Rate.DoesNotExist:
            latest_rate = None

        if latest_rate is None or \
                latest_rate.sale != sale or \
                latest_rate.buy != buy:
            Rate.objects.create(
                base_currency_type=base_currency_type,
                currency_type=currency_type,
                buy=buy,
                sale=sale,
                source=source,
            )
