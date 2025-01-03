from dotenv import load_dotenv
import os
import requests


def get_data(place, forcast_days=None):
    load_dotenv()
    api_key = os.getenv('API_KEY')
    url =f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    res = requests.get(url)
    data = res.json()
    filtered_data = data["list"]
    nr_values = 8 * forcast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Seoul", forcast_days=3, ))

