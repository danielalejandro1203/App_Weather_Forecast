import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_data(place, forecast_days):
    if not API_KEY:
        raise ValueError("API key not found. Please set OPENWEATHER_API_KEY in the .env file.")

    url = (
        "http://api.openweathermap.org/data/2.5/forecast"
        f"?q={place}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    return filtered_data[:nr_values]


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
