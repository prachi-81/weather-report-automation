
import requests


def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_probability_max",
            "weather_code"
        ],
        "forecast_days": 7,
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        return data["daily"]

    except requests.RequestException as error:
        raise RuntimeError(f"Weather API error: {error}")

    except (KeyError, ValueError):
        raise RuntimeError("Invalid weather data received.")
