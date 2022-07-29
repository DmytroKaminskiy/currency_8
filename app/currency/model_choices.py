# # do not import from project
# # from currency.models import Rate
from django.db import models

# CURRENCY_TYPE_UAH = 'UAH'
# CURRENCY_TYPE_USD = 'USD'
# CURRENCY_TYPE_EUR = 'EUR'
# CURRENCY_TYPE_BTC = 'BTC'
#
# CURRENCY_TYPES = (
#     (CURRENCY_TYPE_UAH, 'Hrivna'),
#     (CURRENCY_TYPE_USD, 'Dollar'),
#     (CURRENCY_TYPE_EUR, 'Euro'),
#     (CURRENCY_TYPE_BTC, 'BitCoin'),
# )



class CurrencyType(models.TextChoices):
    CURRENCY_TYPE_UAH = 'UAH', 'Hrivna'
    CURRENCY_TYPE_USD = 'USD', 'Dollar'
    CURRENCY_TYPE_EUR = 'EUR', 'Euro'
    CURRENCY_TYPE_BTC = 'BTC', 'BitCoin'

# class Currency:
#     def __init__(self, code, display):
#         self.code = code
#         self.display = display
#
#
# class CurrencyType2(Currency, models.Choices):
#     CURRENCY_TYPE_UAH = 99, 'UAH', 'Hrivna'
#     # CURRENCY_TYPE_USD = 'USD', 'Dollar'
#     # CURRENCY_TYPE_EUR = 'EUR', 'Euro'
#     # CURRENCY_TYPE_BTC = 'BTC', 'BitCoin'
