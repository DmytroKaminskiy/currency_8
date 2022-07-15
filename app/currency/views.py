from django.http import HttpResponse
from currency.models import Rate


def rate_list(request):

    rates_list = []
    for rate in Rate.objects.all():
        html_string = f'ID: {rate.id}, sale: {rate.sale}, buy: {rate.buy} <br>'
        # breakpoint()
        rates_list.append(html_string)

    return HttpResponse(str(rates_list))


# ORM, models (table), makemigration + migrate