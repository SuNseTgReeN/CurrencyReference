from datetime import datetime

import requests
from django.core.management.base import BaseCommand
from Currency.models import Currency, ExchangeRate


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        data = response.json()
        currencies = data['Valute']

        for currency_code, currency_data in currencies.items():
            char_code = currency_data['CharCode']
            name = currency_data['Name']

            currency, _ = Currency.objects.get_or_create(char_code=char_code, name=name)

            rate_date_str = data['Date']
            rate_date = datetime.strptime(rate_date_str, '%Y-%m-%dT%H:%M:%S%z').date()
            rate_value = currency_data['Value']

            ExchangeRate.objects.get_or_create(currency=currency, date=rate_date, value=rate_value)
