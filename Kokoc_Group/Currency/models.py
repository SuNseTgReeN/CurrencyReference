from django.db import models
from django.db.models import UniqueConstraint

from django.utils.translation import gettext_lazy as _


class Currency(models.Model):
    char_code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.char_code

    class Meta:
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencys')


class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        verbose_name = _('Exchange rate')
        verbose_name_plural = _('Exchange rate')
        constraints = [
            UniqueConstraint(fields=['currency', 'date'], name='unique_currency_date')
        ]

    def __str__(self):
        return f"{self.currency} - {self.date}"
