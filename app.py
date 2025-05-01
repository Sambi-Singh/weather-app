import requests
api_key = 'e447e1949ba12f16e9d1d8349855896f'

city = input("Enter city: ")
#print(user_input)

location_data = requests.get(
    f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}")

print(location_data.json())
#print(weather_data.status_code)