import requests
url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_demo_key&currencies=TRY,USD"
data = requests.get(url).json()
print(f"1 USD = {data['data']['TRY']:.2f} TRY")