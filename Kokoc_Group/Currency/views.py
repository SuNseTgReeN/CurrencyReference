from datetime import datetime
from django.views.generic import ListView
from Currency.models import ExchangeRate


class ShowRatesView(ListView):
    model = ExchangeRate
    template_name = 'show_rates.html'
    context_object_name = 'exchange_rates'

    def get_queryset(self):
        rate_date_str = self.request.GET.get('date')
        rate_date = datetime.strptime(rate_date_str, '%Y-%m-%d').date()
        queryset = super().get_queryset()

        if rate_date_str:
            queryset = queryset.filter(date=rate_date)
        return queryset
