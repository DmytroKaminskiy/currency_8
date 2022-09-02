from currency import consts
from currency.models import Source


def get_or_create_privatbank_source():
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'

    source = Source.objects.get_or_create(
        code_name=consts.CODE_NAME_PRIVATBANK,
        defaults={'url': url, 'name': 'PrivatBank'},
    )[0]
    return source
