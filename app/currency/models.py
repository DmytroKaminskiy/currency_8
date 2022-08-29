from django.db import models
from currency.model_choices import CurrencyType


class CreatedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Source(CreatedModel):
    url = models.URLField()
    name = models.CharField(max_length=256, unique=True)
    code_name = models.CharField(max_length=16, unique=True)


class Rate(CreatedModel):
    # def get_{field_name}_display() if field has choices
    base_currency_type = models.CharField(
        max_length=3,
        choices=CurrencyType.choices,
        default=CurrencyType.CURRENCY_TYPE_USD,
    )
    currency_type = models.CharField(max_length=3, choices=CurrencyType.choices)
    sale = models.DecimalField(max_digits=10, decimal_places=4)
    buy = models.DecimalField(max_digits=10, decimal_places=4)
    # source = models.ForeignKey(Source)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE, related_name='rates')

    # def save(self):
    #     super().save()

    # class Meta:
    #     ordering = ...
    #  prefetch_related


class ContactUs(CreatedModel):
    subject = models.CharField(max_length=128)
    body = models.CharField(max_length=1024)
    from_email = models.EmailField()
    to_email = models.EmailField()
