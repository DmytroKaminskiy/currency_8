from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404

from currency.models import Rate
from currency.forms import RateForm

# context_processor - GLOBAL Context - base.html

def index(request):
    return render(request, 'currency/index.html')


def rate_list(request):
    context = {
        'rate_list': Rate.objects.all(),
    }
    return render(request, 'currency/rate_list.html', context=context)  # rate_list.html


def rate_create(request):

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm()

    context = {'form': form}
    return render(request, 'currency/rate_create.html', context=context)


def rate_update(request, rate_id):
    '''
    /rate/update/?id=12
    /rate/update/12/
    '''

    # try:
    #     rate_instance = Rate.objects.get(id=rate_id)
    # except Rate.DoesNotExist:
    #     raise Http404

    rate_instance = get_object_or_404(Rate, id=rate_id)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm(instance=rate_instance)

    context = {'form': form}
    return render(request, 'currency/rate_update.html', context=context)


def rate_details(request, rate_id):
    rate_instance = get_object_or_404(Rate, id=rate_id)
    context = {'instance': rate_instance}
    return render(request, 'currency/rate_details.html', context=context)


def rate_delete(request, rate_id):
    rate_instance = get_object_or_404(Rate, id=rate_id)

    if request.method == 'POST':
        rate_instance.delete()
        return HttpResponseRedirect('/rate/list/')

    context = {'instance': rate_instance}
    return render(request, 'currency/rate_delete.html', context=context)


# def get_form(request):
#     form1 = Form()
#     form2 = Form()
#     context = {
#         'form1': form1,
#         'form2': form2,
#     }
#     return render()
#
# def post_form1(request):  # /form1/
#     pass
#
# def post_form2(request): # /form2/
#     pass

# /source/rate/bank/details/

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

'''
GET - retrieve from server http://localhost/?age=30&firstName=Dima
POST - send data to server

http://localhost/

age=30&firstName=Dima


GET - read
POST - create
PUT/PATCH - Update
DELETE - Delete

OPTIONS - get all available methods
HEAD - GET without body (Content-Length)


/rate/25/ - GET, PUT, DELETE

/rate/25/get/
/rate/25/create/
/rate/25/delete/



'''
