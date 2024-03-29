from rest_framework.serializers import ModelSerializer

from currency.models import Rate


class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'currency_type',
            'base_currency_type',
            'created',
            'source',
        )
