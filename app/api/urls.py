from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

app_name = 'api'

router = DefaultRouter()
router.register('rates', views.RateViewSet, basename='rate')

urlpatterns = [
    # path('rates/', views.RatesView.as_view(), name='rates'),
    # path('rates/<int:pk>/', views.RateDetailsView.as_view(), name='rate-details'),
]

urlpatterns += router.urls
