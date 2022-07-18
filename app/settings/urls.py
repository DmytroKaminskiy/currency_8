from django.contrib import admin
from django.urls import path

from currency.views import rate_list, index, http_response

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index),
    path('rate/list/', rate_list),
    path('response/', http_response),
]
