import requests

# OpenWeatherMap API configuration
API_KEY = 'your_openweathermap_api_key'
CITY = 'Your City'  # Replace with your city name
UNITS = 'metric'    # Use 'metric' for Celsius, 'imperial' for Fahrenheit, or 'standard' for Kelvin

def get_weather_forecast():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&units={UNITS}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return weather, temperature
    else:
        return None, None

def suggest_outfit(weather, temperature):
    if temperature >= 25:
        outfit = "Wear light clothes, like a T-shirt and light pants."
    elif temperature >= 15:
        outfit = "A light sweater or jacket with jeans would be great."
    else:
        outfit = "Don't forget to wear a warm coat and scarf!"

    return outfit

if __name__ == "__main__":
    weather, temperature = get_weather_forecast()

    if weather and temperature:
        outfit_suggestion = suggest_outfit(weather, temperature)
        print(f"The weather in {CITY} today is {weather} with a temperature of {temperature}°C.")
        print("Here's an outfit suggestion for you:")
        print(outfit_suggestion)
    else:
        print("Failed to retrieve weather data. Please check your API key and city name or internet connection.")
