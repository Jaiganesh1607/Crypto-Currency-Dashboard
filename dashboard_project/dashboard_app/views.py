import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def dashboard_view(request):
    try:
        # Top 5 cryptocurrencies by market cap
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 5,
            'page': 1,
            'sparkline': 'false'
        }
        response = requests.get(url, params=params)
        top_coins = response.json()

        # Trending coins (names + icons)
        trending_url = "https://api.coingecko.com/api/v3/search/trending"
        trending_response = requests.get(trending_url)
        trending_data = trending_response.json()

        trending_coins = []
        for item in trending_data.get("coins", []):
            coin = item.get("item", {})
            trending_coins.append({
                'name': coin.get("name"),
                'symbol': coin.get("symbol"),
                'icon': coin.get("small")
            })

        # Pie chart: market cap of top 5 coins
        pie_labels = [coin["name"] for coin in top_coins]
        pie_values = [coin["market_cap"] for coin in top_coins]

        # Line chart: price history for Bitcoin (last 7 days, daily)
        btc_chart_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
        btc_chart_params = {'vs_currency': 'usd', 'days': 7}
        btc_response = requests.get(btc_chart_url, params=btc_chart_params)
        btc_prices = btc_response.json().get("prices", [])

        btc_dates = [point[0] for point in btc_prices]
        btc_values = [point[1] for point in btc_prices]

        bar_labels = [coin['name'] for coin in top_coins]
        bar_values = [coin['price_change_percentage_24h'] for coin in top_coins]

        data = {
            'top_coins': top_coins,
            'trending_coins': trending_coins,
            'pie_labels': pie_labels,
            'pie_values': pie_values,
            'btc_dates': btc_dates,
            'btc_values': btc_values,
            'bar_labels': bar_labels,
            'bar_values': bar_values,
        }

        return render(request, 'dashboard_app/home.html', {'data': data})

    except Exception as e:
        print("Error fetching data:", e)
        return render(request, 'errors/500.html', status=500)


def error_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)

def error_500_view(request):
    return render(request, 'errors/500.html', status=500)
