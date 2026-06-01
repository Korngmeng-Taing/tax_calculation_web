from tax_calculators.currency_utils import get_exchange_rate, get_currency_symbol


def exchange_rate(request):
    rate = get_exchange_rate('USD')
    return {
        'exchange_rate': float(rate),
        'exchange_rate_display': f"1 USD = {rate:,.0f} KHR",
        'khr_symbol': get_currency_symbol('KHR'),
        'usd_symbol': get_currency_symbol('USD'),
    }
