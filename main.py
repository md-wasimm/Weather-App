import requests
import json
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

city = input("Enter the city name: \n")

url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey=mNHvHvsyHKthYlXhtswJlfathkeH8HA8"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
t = wdic["data"]["values"]["temperature"]
h = wdic["data"]["values"]["humidity"]
w = wdic["data"]["values"]["windSpeed"]
print(f"Temperature: {t} Degrees")
print(f"Humidity: {h}")
print(f"Wind Speed: {w} Km/Hour")
speaker.speak(f"The current temperature in {city} is {t} degrees and humidity is {h} and wind speed is {w} km per hour")