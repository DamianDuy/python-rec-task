from django.test import Client, TestCase
from django.urls import resolve, reverse

from currency_app.models import Currency, CurrencyRate

from .views import CurrencyRateView, CurrencyView


class CurrencyViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_currency_get(self):
        url = reverse("currency")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(CurrencyView, resolve(url).func.view_class)


class CurrencyRateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.currency_rate_obj = CurrencyRate.objects.get(
            currency_from=Currency.objects.get(code="PLN"),
            currency_to=Currency.objects.get(code="USD"),
        )

    def test_currency_rate(self):
        url = reverse(
            "currency_rate",
            kwargs={
                "currency_from_code": self.currency_rate_obj.currency_from.code,
                "currency_to_code": self.currency_rate_obj.currency_to.code,
            },
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(CurrencyRateView, resolve(url).func.view_class)

    def test_currency_rate_url_invalid_first_arg(self):
        url = reverse(
            "currency_rate",
            kwargs={
                "currency_from_code": "ERR",
                "currency_to_code": self.currency_rate_obj.currency_to.code,
            },
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_currency_rate_url_invalid_second_arg(self):
        url = reverse(
            "currency_rate",
            kwargs={
                "currency_from_code": self.currency_rate_obj.currency_from.code,
                "currency_to_code": "ERR",
            },
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_currency_rate_url_invalid_both_args(self):
        url = reverse(
            "currency_rate",
            kwargs={
                "currency_from_code": "ER1",
                "currency_to_code": "ER2",
            },
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
