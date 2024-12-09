from django.urls import path

from currency_app.views import CurrencyRateView, CurrencyView

urlpatterns = [
    path("currency/", CurrencyView.as_view(), name="currency"),
    path(
        "currency/<str:currency_from_code>/<str:currency_to_code>/",
        CurrencyRateView.as_view(),
        name="currency_rate",
    ),
]
