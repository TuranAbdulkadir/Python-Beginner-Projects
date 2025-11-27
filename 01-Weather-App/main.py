import requests
API_KEY = "bd5e378503939ddaee76f12ad7a97608"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
city = input("Enter city name: ")
url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric&lang=en"
res = requests.get(url)
if res.status_code == 200:
    data = res.json()
    print(f"Weather in {city}: {data['weather'][0]['description']}, {data['main']['temp']}°C")
else:
    print("City not found.")