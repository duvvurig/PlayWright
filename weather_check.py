from playwright.sync_api import sync_playwright
import requests

def get_city_coordinates(city):
    """Use Open-Meteo geocoding API to get latitude & longitude of a city."""
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    response = requests.get(geo_url, params={"name": city})

    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        raise ValueError("City not found!")

    city_info = data["results"][0]
    return city_info["latitude"], city_info["longitude"]


def check_weather(city):
    # Get coordinates of the city
    lat, lon = get_city_coordinates(city)
    print(f"Coordinates for {city}: {lat}, {lon}")

    weather_url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    # Use Playwright for API request
    with sync_playwright() as p:
        request_context = p.request.new_context()
        response = request_context.get(weather_url, params=params)

        print("Status Code:", response.status)
        data = response.json()
        print("Weather API Response:", data)

        # Assertions
        assert response.status == 200, "Weather API call failed!"
        assert "current_weather" in data, "Missing weather data!"

        temperature = data["current_weather"]["temperature"]
        print(f"🌤 Current temperature in {city}: {temperature}°C")


if __name__ == "__main__":
    city_name = input("Enter city name: ")
    check_weather(city_name)
