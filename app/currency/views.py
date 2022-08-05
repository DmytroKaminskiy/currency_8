from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail

from django.views import generic

from currency.models import Rate, ContactUs
from currency.forms import RateForm
from currency.model_choices import CurrencyType

# from settings import settings BAD
from django.conf import settings

# context_processor - GLOBAL Context - base.html

# def index(request):
#     return render(request, 'currency/index.html')


class IndexView(generic.TemplateView):
    template_name = 'currency/index.html'

    def get_context_data(self, **kwargs) -> dict:
        context: dict = super().get_context_data(**kwargs)
        context['rate_count'] = Rate.objects.count()
        return context


class RateListView(generic.ListView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_list.html'

    # def get_context_data(self, *args, **kwargs):
    #     Rate.objects.last()
    #     return super().get_context_data(*args, **kwargs)


class RateCreateView(generic.CreateView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_create.html'
    form_class = RateForm
    # success_url = '/rate/list/'
    success_url = reverse_lazy('currency:rate_list')
    initial = {'currency_type': CurrencyType.CURRENCY_TYPE_EUR}

    # def get(self, request, **kwargs):
    #     return super().get(request, **kwargs)


class RateUpdateView(generic.UpdateView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_update.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')


class RateDeleteView(generic.DeleteView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_delete.html'
    success_url = reverse_lazy('currency:rate_list')

class RateDetailsView(generic.DeleteView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_details.html'


class ContactUsCreateView(generic.CreateView):
    model = ContactUs
    success_url = reverse_lazy('currency:rate_list')
    template_name = 'currency/contactus_create.html'
    fields = (
        'from_email',
        'subject',
        'body',
    )

    def form_valid(self, form):
        response = super().form_valid(form)

        # form.cleaned_data
        # self.object

        subject = 'ContactUs From Currency Project'
        body = f'''
        Subject From Client: {self.object.subject}
        Email: {self.object.from_email}
        Wants to contact
        '''

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return response

# def rate_list(request):
#     context = {
#         'rate_list': Rate.objects.all(),
#     }
#     return render(request, 'currency/rate_list.html', context=context)  # rate_list.html
#
#
# def rate_create(request):
#
#     if request.method == 'POST':
#         form = RateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('rate_list'))  # HttpResponseRedirect('/rate/list/')
#     elif request.method == 'GET':
#         form = RateForm()
#
#     context = {'form': form}
#     return render(request, 'currency/rate_create.html', context=context)
#
#
# def rate_update(request, rate_id):
#
#     rate_instance = get_object_or_404(Rate, id=rate_id)
#
#     if request.method == 'POST':
#         form = RateForm(request.POST, instance=rate_instance)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/rate/list/')
#     elif request.method == 'GET':
#         form = RateForm(instance=rate_instance)
#
#     context = {'form': form}
#     return render(request, 'currency/rate_update.html', context=context)
#
#
# def rate_details(request, rate_id):
#     rate_instance = get_object_or_404(Rate, id=rate_id)
#     context = {'instance': rate_instance}
#     return render(request, 'currency/rate_details.html', context=context)
#
#
# def rate_delete(request, rate_id):
#     rate_instance = get_object_or_404(Rate, id=rate_id)
#
#     if request.method == 'POST':
#         rate_instance.delete()
#         return HttpResponseRedirect('/rate/list/')
#
#     context = {'instance': rate_instance}
#     return render(request, 'currency/rate_delete.html', context=context)


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

# def foo(request):
#     path = request.GET.get('path')
#     '../../../../../../../etc/conf'
#     with open(path) as file:
#         ...
