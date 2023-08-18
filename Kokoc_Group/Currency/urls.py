from django.urls import path

from Currency.views import ShowRatesView

app_name = 'Currency'

urlpatterns = [
    path('show_rates/', ShowRatesView.as_view(), name='exchange_rates'),
]
