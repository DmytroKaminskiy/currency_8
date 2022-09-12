from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from drf_excel.renderers import XLSXRenderer
from drf_excel.mixins import XLSXFileMixin

from api.serializers import RateSerializer
from currency.models import Rate


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


class RateViewSet(XLSXFileMixin, ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    renderer_classes = [JSONRenderer, XLSXRenderer]
    filename = 'my_export.xlsx'
