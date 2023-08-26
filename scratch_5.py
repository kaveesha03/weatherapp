
import requests


def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    return weather_data


def main():
    api_key = "d8bed35f8ab93b38799b398571dc9104"
    city = input("Enter a city name: ")

    weather_data = get_weather(city, api_key)

    if weather_data["cod"] == 200:
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
    else:
        print("City not found or an error occurred.")


if __name__ == "__main__":
    main()


