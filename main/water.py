import requests

url = "https://api.meersens.com/environment/public/water/current"
params = {
    "lat": 1.234,
    "lng": 5.678
}
headers = {
    "apikey": "your_api_key"
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    water_quality_data = response.json()
else:
    print("Error fetching data from API.")

import matplotlib.pyplot as plt

# Assuming you have the water quality data in a variable named water_quality_data

# Extracting pH values and corresponding datetimes
pH_values = [entry['pollutants']['pH']['value'] for entry in water_quality_data]
datetimes = [entry['datetime'] for entry in water_quality_data]

# Convert datetime strings to datetime objects (if needed)
# This step may not be necessary if the datetime format is already recognized
# Example: Convert ISO format to datetime
# datetimes = [datetime.datetime.fromisoformat(dt) for dt in datetimes]

# Create a line plot
plt.plot(datetimes, pH_values, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Datetime')
plt.ylabel('pH Value')
plt.title('Water pH Over Time')

# Rotate x-axis labels for better visibility (optional)
plt.xticks(rotation=45)

# Show the plot
plt.show()
import matplotlib.pyplot as plt

# Assuming you have the water quality data in a variable named water_quality_data

# Extracting pH values and corresponding datetimes
pH_values = [entry['pollutants']['pH']['value'] for entry in water_quality_data]
datetimes = [entry['datetime'] for entry in water_quality_data]

# Convert datetime strings to datetime objects (if needed)
# This step may not be necessary if the datetime format is already recognized
# Example: Convert ISO format to datetime
# datetimes = [datetime.datetime.fromisoformat(dt) for dt in datetimes]

# Create a line plot
plt.plot(datetimes, pH_values, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Datetime')
plt.ylabel('pH Value')
plt.title('Water pH Over Time')

# Rotate x-axis labels for better visibility (optional)
plt.xticks(rotation=45)

# Show the plot
plt.show()

