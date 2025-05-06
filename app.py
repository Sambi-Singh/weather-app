import requests
api_key = 'e447e1949ba12f16e9d1d8349855896f'

city = input("Enter city: ")
#print(user_input)

location_data = requests.get(
    f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}")


#print(location_data.json())
lon = location_data.json() [0]['lon']
lat = location_data.json() [0]['lat']
#print(lat)
#print(lon)

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}")
#print(weather_data.status_code)
#print(weather_data.json())
weather = weather_data.json()['weather'][0]['main']
print(f"The weather in {city} right now is {weather}")