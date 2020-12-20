import random
from datetime import datetime
import json

imgurCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
def get_imgur_url():
    imgur_url = "http://i.imgur.com/"
    ext = ".jpg"
    code = ""
    limit = random.choice([5,6,7])
    for _ in range(0, limit):
        code += random.choice(imgurCharacters)

    full_url = imgur_url + code + ext
    return full_url

def getTempEmoji(temp: float):
    if temp < -10:
        return ":cold_face:"
    elif temp < 0:
        return ":snowman2:"
    elif temp < 15:
        return ":leaves:"
    elif temp < 25:
        return ":beach:"
    elif temp < 35:
        return ":hot_face:"
    else:
        return ":volcano:"

def process_weather_data(data: json, location: str):

    temp = data["temp"]
    temperatureEmoji = getTempEmoji(temp)

    #print(data)

    sr   = data["sunrise"]
    ss   = data["sunset"]

    sunrise = datetime.utcfromtimestamp(sr).strftime('%H:%M')
    sunset  = datetime.utcfromtimestamp(ss).strftime('%H:%M')

    return "Current weather in {city}: {temp} °C {temoji} with a sunrise :sunrise: at {sunrise} and a sunset :city_sunset: at {sunset}"\
    .format(city = location, temp = temp, temoji = temperatureEmoji, sunrise = sunrise, sunset = sunset)
