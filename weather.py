import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv() # Load environment variables from .env file

def get_current_weather(city="Trondheim"):

    request_url= f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'

    #print(f"\nRequest URL: {request_url}\n")

    weather_data = requests.get(request_url).json()
    
    return weather_data

if __name__ == '__main__':
    print("\n***Get Weather Conditions***\n")
    city = input("\nPlease enter a city name: ")

    #Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "Trondheim"
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
