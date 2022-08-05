from django.contrib import admin
from currency.models import Rate

from rangefilter.filters import DateTimeRangeFilter


class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'base_currency_type',
        'currency_type',
        'sale',
        'buy',
    )
    readonly_fields = (
        'sale',
        'buy',
    )
    search_fields = (
        'base_currency_type',
        'currency_type',
        'sale',
        'buy',
    )
    list_filter = (
        'base_currency_type',
        ('created', DateTimeRangeFilter),
    )
    # def has_change_permission(self, request, obj=None):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False

    # class Meta:
    #     verbose_name = ...

admin.site.register(Rate, RateAdmin)
