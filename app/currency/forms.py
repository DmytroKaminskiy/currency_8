from django import forms
from currency.models import Rate

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'base_currency_type',
            'currency_type',
            'sale',
            'buy',
            'source',
        )
        # widgets = {}

    # def __init__(self):
    #     super().__init__()
    #     breakpoint()

# class Student:
#     pass
#
# st1 = Student()