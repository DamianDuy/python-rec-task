import yfinance as yf
from django.db import migrations


def insert_currencies(apps, _schema_editor):
    currency_codes = ["USD", "EUR", "PLN", "JPY"]
    Currency = apps.get_model("currency_app", "Currency")
    CurrencyRate = apps.get_model("currency_app", "CurrencyRate")

    for currency_from_code in currency_codes:
        currency_from, _ = Currency.objects.get_or_create(code=currency_from_code)

        for currency_to_code in currency_codes:
            if currency_from_code == currency_to_code:
                continue

            ticker = yf.Ticker(f"{currency_from_code}{currency_to_code}=X")
            currency_to, _ = Currency.objects.get_or_create(code=currency_to_code)

            CurrencyRate.objects.create(
                currency_from=currency_from,
                currency_to=currency_to,
                rate=ticker.info["bid"],
            )


class Migration(migrations.Migration):
    dependencies = [
        ("currency_app", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(insert_currencies),
    ]
