from django.test import TestCase

from currency_app.models import Currency, CurrencyRate


class CurrencyTest(TestCase):
    def setUp(self):
        self.currency_codes = ["USD", "EUR", "PLN", "JPY"]
        return super().setUp()

    def test_retrieve_currency_objects(self):
        for code in self.currency_codes:
            self.assertIsNotNone(Currency.objects.get(code=code))

    def test_currency_object_not_exist_response(self):
        with self.assertRaises(Currency.DoesNotExist):
            Currency.objects.get(code="ERR")


class CurrencyRateTest(TestCase):
    def setUp(self):
        self.currency_codes = ["USD", "EUR", "PLN", "JPY"]
        return super().setUp()

    def test_retrieve_currency_rates_objects(self):
        for currency_from_code in self.currency_codes:
            currency_from = Currency.objects.get(code=currency_from_code)

        for currency_to_code in self.currency_codes:
            if currency_from_code != currency_to_code:
                currency_to = Currency.objects.get(code=currency_to_code)
                self.assertIsNotNone(
                    CurrencyRate.objects.get(
                        currency_from=currency_from, currency_to=currency_to
                    )
                )

    def test_currency_rates_object_not_exist_response(self):
        with self.assertRaises(CurrencyRate.DoesNotExist):
            CurrencyRate.objects.get(
                currency_from=Currency.objects.get(code="PLN"),
                currency_to=Currency.objects.get(code="PLN"),
            )
