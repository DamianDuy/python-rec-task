from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    rates = models.ManyToManyField("self", symmetrical=False, through="CurrencyRate",
                                   through_fields=("currency_from", "currency_to"))

class CurrencyRate(models.Model):
    currency_from = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="currency_from")
    currency_to = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="currency_to")
    rate = models.FloatField()
