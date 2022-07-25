from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from currency import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.IndexView.as_view()),

    path('currency/', include('currency.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
