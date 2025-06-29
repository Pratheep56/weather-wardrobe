import requests

def get_outfit_recommendation(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch weather for {city}: {response.text}")
    data = response.json()
    temp = data["main"]["temp"]
    condition = data["weather"][0]["main"].lower()

    if temp < 10:
        outfit = "a warm jacket and a scarf"
    elif temp < 20:
        outfit = "a light sweater"
    else:
        outfit = "a t-shirt"

    if 'rain' in condition:
        outfit += " and bring an umbrella"
    elif 'clear' in condition and temp > 15:
        outfit += " and sunglasses"

    return f"You should wear {outfit}."
