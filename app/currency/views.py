from django.http import HttpResponse
from django.shortcuts import render

from currency.models import Rate

# context_processor - GLOBAL Context - base.html

def index(request):
    return render(request, 'index.html')


def rate_list(request):
    context = {
        'rate_list': Rate.objects.all(),
    }
    return render(request, 'rate_list.html', context=context)  # rate_list.html


def http_response(request):
    '''
    1xx - Info
    2xx - Success
    3xx - Redirect
    4xx - Client error
    5xx - Server error

    200 - OK
    201 - Created
    202 - Accepted
    204	- No Content

    301 - Permanently
    307	- Temporary Redirect

    400 - Bad Request
    401 - Unauthorized
    403 - Forbidden
    404	- Not Found
    405	- Method Not Allowed

    500 - Internal Server Error
    502	- Bad Gateway
    '''
    return HttpResponse('EXAMPLE', status=200)
