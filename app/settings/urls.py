from django.contrib import admin
from django.urls import path

from currency.views import rate_list, index, http_response, rate_create, rate_update, rate_details, rate_delete

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index),
    path('rate/list/', rate_list),
    path('rate/create/', rate_create),
    path('rate/update/<int:rate_id>/', rate_update),
    path('rate/details/<int:rate_id>/', rate_details),
    path('rate/delete/<int:rate_id>/', rate_delete),
    path('response/', http_response),
]
