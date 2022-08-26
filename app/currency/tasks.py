from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def slow_func():
    from time import sleep
    print('START')
    sleep(10)
    print('END')


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
