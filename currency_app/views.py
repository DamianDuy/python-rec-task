from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from currency_app.models import Currency, CurrencyRate


class CurrencyView(View):
    def get(self, request, *args, **kwargs):
        order = request.GET.get("order")
        starts_with = request.GET.get("startsWith")
        ends_with = request.GET.get("endsWith")

        currencies = Currency.objects.all()

        if order == "asc":
            currencies = currencies.order_by("code")
        elif order == "desc":
            currencies = currencies.order_by("-code")

        if starts_with is not None and starts_with != "":
            currencies = currencies.filter(code__istartswith=starts_with)

        if ends_with is not None and ends_with != "":
            currencies = currencies.filter(code__iendswith=ends_with)

        payload = []

        for currency in currencies:
            payload.append({"code": currency.code})

        return JsonResponse(payload, safe=False)


class CurrencyRateView(View):
    def get(self, request, *args, **kwargs):
        currency_from = get_object_or_404(
            Currency, pk=self.kwargs["currency_from_code"]
        )
        currency_to = get_object_or_404(Currency, pk=self.kwargs["currency_to_code"])

        currency_rate = get_object_or_404(
            CurrencyRate, currency_from=currency_from, currency_to=currency_to
        )

        return JsonResponse(
            {
                "currency_pair": f"{currency_from.code}{currency_to.code}",
                "exchange_rate": currency_rate.rate,
            }
        )
