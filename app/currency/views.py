import csv
import io
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views import generic
# from settings import settings BAD
from django.conf import settings

from currency.resources import RateResource
from currency.models import Rate, ContactUs
from currency.forms import RateForm
from currency.model_choices import CurrencyType
from django.contrib.sessions.models import Session

from currency.tasks import send_contact_us_email


# context_processor - GLOBAL Context - base.html

# def index(request):
#     return render(request, 'currency/index.html')


class IndexView(generic.TemplateView):
    template_name = 'currency/index.html'

    def get_context_data(self, **kwargs) -> dict:
        context: dict = super().get_context_data(**kwargs)
        context['rate_count'] = Rate.objects.count()
        return context


# class RateListView(UserPassesTestMixin, generic.ListView):
class RateListView(generic.ListView):
    queryset = Rate.objects.all().select_related('source')
    template_name = 'currency/rate_list.html'
    # raise_exception = True

    # def get_context_data(self, *args, **kwargs):
    #     Rate.objects.last()
    #     return super().get_context_data(*args, **kwargs)

    # def test_func(self):
    #     return False
    #     return self.request.user.is_superuser


class RateCreateView(generic.CreateView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_create.html'
    form_class = RateForm
    # success_url = '/rate/list/'
    success_url = reverse_lazy('currency:rate_list')
    initial = {'currency_type': CurrencyType.CURRENCY_TYPE_EUR}

    # def get_form_class(self):
    #     if self.request.user.is_authenticated:
    #         return RateForm
    #     else:
    #         return RateForm2

    # def get(self, request, **kwargs):
    #     return super().get(request, **kwargs)


class RateUpdateView(generic.UpdateView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_update.html'
    form_class = RateForm  # is_valid()
    success_url = reverse_lazy('currency:rate_list')


class RateDeleteView(generic.DeleteView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_delete.html'
    success_url = reverse_lazy('currency:rate_list')

class RateDetailsView(generic.DeleteView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_details.html'


class DownloadRateView(generic.View):
    # def get(self, request):
    #     csv_content = RateResource().export().csv
    #     return HttpResponse(csv_content, content_type='text/csv')
    def get__(self, request):
        with open('rate.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            headers = ['id', 'buy', 'sale']
            spamwriter.writerow(headers)
            for rate in Rate.objects.all():
                row = [
                    rate.id,
                    rate.buy,
                    rate.sale,
                ]
                spamwriter.writerow(row)

        with open('rate.csv', 'r') as f:
            file_data = f.read()

        return HttpResponse(file_data, content_type='text/csv')

    def get(self, request):
        csvfile = io.StringIO()
        spamwriter = csv.writer(csvfile)
        headers = ['id', 'buy', 'sale']
        spamwriter.writerow(headers)
        for rate in Rate.objects.all():
            row = [
                rate.id,
                rate.buy,
                rate.sale,
            ]
            spamwriter.writerow(row)

        csvfile.seek(0)
        return HttpResponse(csvfile.read(), content_type='text/csv')


class ContactUsCreateView(generic.CreateView):
    model = ContactUs
    success_url = reverse_lazy('currency:rate_list')
    template_name = 'currency/contactus_create.html'
    fields = (
        'from_email',
        'subject',
        'body',
    )

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['body'].widget = forms.Textarea()
        return form

    def form_valid(self, form):
        response = super().form_valid(form)

        # form.cleaned_data
        # self.object

        send_contact_us_email.delay(self.object.subject, self.object.from_email)

        return response



# TODO move to accounts app
class UserProfileView(LoginRequiredMixin, generic.UpdateView):
    queryset = get_user_model().objects.all()
    template_name = 'currency/my_profile.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
        'avatar',
    )

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(id=self.request.user.id)
    #     return queryset

    def get_object(self, queryset=None):
        # super().get_object()
        return self.request.user

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


Recursive
'''

# def foo(request):
#     path = request.GET.get('path')
#     '../../../../../../../etc/conf'
#     with open(path) as file:
#         ...
