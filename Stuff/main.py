"""
Requests module provides access to websites or APIs so that you can get data
"""
import requests

# Ask the user for a keyword (e.g., "Mars", "Hubble", "Earth")
nasa_search = input("Enter a space related word: ").strip().title()

# Generate the NASA Image and Video Library API URL
URL = f"https://images-api.nasa.gov/search?q={nasa_search}&media_type=image"

# Use requests module to make an API call and get the data
# Note: Data will come back as a JSON object
json_data = requests.get(URL, timeout=10).json()

# Get the first image URL from the results
items = json_data.get("collection", {}).get("items", [])
nasa_image = items[0]["links"][0]["href"] if items else "No image found."

print(nasa_image)
