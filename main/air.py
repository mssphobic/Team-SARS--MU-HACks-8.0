import requests

# Define the URL with placeholders for latitude, longitude, start date, end date, and API key
url = "http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}&appid={API_key}"

# Replace placeholders with actual values
url = url.format(lat=50, lon=50, start=1606223802, end=1606482999, API_key="70ade92ad2eae7b737b3eac093ad5cd5")

# Make the request
response = requests.get(url)

if response.status_code == 200:
    air_pollution_data = response.json()
    # Process the air pollution data here
    print(air_pollution_data)
else:
    print(f"Error: {response.status_code}")








