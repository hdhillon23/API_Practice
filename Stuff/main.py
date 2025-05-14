"""
Requests module provides access to websites or API's sp that you can get data
"""
import requests

city_name = input("What city? ").strip().lower()

# Enter your API key
API_KEY = "5572a4c7acad6e1ff8bc2f581a03f85e"

# Generate the URL needed for thr API call
URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

# USe requests module to make an API call and get the data
## Note: data will come back as a JSON object
json_data = requests.get(URL, timeout=10).json()

# Get the conditions
forecast = json_data['weather'][0]['description']

print(forecast)
