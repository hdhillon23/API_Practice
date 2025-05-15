"""
Requests module provides access to websites or API's sp that you can get data
"""
import requests

city_name = input("What city? ").strip().lower()

# Enter your API key
API_KEY = "5572a4c7acad6e1ff8bc2f581a03f85e"

# Generate the URL needed for thr API call
URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

# Use requests module to make an API call and get the data
## Note: data will come back as a JSON object
json_data = requests.get(URL, timeout=10).json()

# Get the conditions
forecast = json_data['weather'][0]['description']

#Get the temperature
temp = json_data["main"]["feels_like"]
temp_c = temp  - 273.15
temp_c = round(temp_c, 1)

print(f"At this moment, it is {temp_c}°C in {city_name.title()}. The forecast is {forecast}.")