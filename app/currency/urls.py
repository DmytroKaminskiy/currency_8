from django.urls import path
from currency import views

app_name = 'currency'


urlpatterns = [
    path('rate/list/', views.RateListView.as_view(), name='rate_list'),
    path('rate/create/', views.RateCreateView.as_view(), name='rate_create'),
    path('rate/update/<int:pk>/', views.RateUpdateView.as_view(), name='rate_update'),
    path('rate/delete/<int:pk>/', views.RateDeleteView.as_view(), name='rate_delete'),
    path('rate/details/<int:pk>/', views.RateDetailsView.as_view(), name='rate_details'),
    path('rate/download/', views.DownloadRateView.as_view(), name='rate_download'),
    path('contactus/create/', views.ContactUsCreateView.as_view(), name='contactus_create'),
    # path('my-profile/<int:pk>/', views.UserProfileView.as_view(), name='my_profile'),
    path('my-profile/', views.UserProfileView.as_view(), name='my_profile'),

    # path('api/example/', views.api_get_rates_list),
]
