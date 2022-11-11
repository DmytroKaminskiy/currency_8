from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from drf_excel.renderers import XLSXRenderer
from drf_excel.mixins import XLSXFileMixin

from api.v1.filters import RateFilter
from api.v1.pagination import RatePagination
from api.v1.serializers import RateSerializer
from api.v1.throttles import AnonRateModelThrottle, AnonSourceThrottle
from currency.models import Rate, Source

# class RatesView(generics.ListAPIView, generics.CreateAPIView):
# class RatesView(generics.ListCreateAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer
#
#
# class RateDetailsView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer

# CRUD

# [1..20]
# limit 5 offset 10
# [11..15]

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters


class RateViewSet(XLSXFileMixin, ModelViewSet):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer
    renderer_classes = [JSONRenderer, XLSXRenderer]
    filename = 'my_export.xlsx'
    pagination_class = RatePagination

    filterset_class = RateFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    ordering_fields = ['id', 'buy', 'sale']
    throttle_classes = [AnonRateModelThrottle]


class SourceViewSet(ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = RateSerializer
    throttle_classes = [AnonSourceThrottle]
