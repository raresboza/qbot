import requests
import json
import discord
import random
from discord.ext import commands
from datetime import datetime

client = commands.Bot(command_prefix = '$')
bullyMagnet = ['De ce incerci?', 'Ba ?','Voi il vedeti pe asta ba @everyone', 'Iesi acasa', 'Iesi', 'Nu te-ai futut cu Andone nu?']
citiesCoord = {
    "galati": (45.437572, 27.907411),
    "groningen": (53.219383, 6.566501),
    "braila": (45.265246, 27.959471),
    "bucuresti": (44.439663, 26.096306),
    "londra": (51.507350, -0.127758),
    "leeds": (53.79648, -1.54785),
    "cluj": (46.770439, 23.591423)
}

@client.command("weather")
async def _weather(ctx, args=""):
    if len(args.split()) != 1:
        await ctx.send("Weather command excepts only one argument!:grimacing:")
    else:
        city = args.lower()
        if citiesCoord.get(city) is None:
            await ctx.send("In our gargantuos data base the city of {} wasnt found".format(city))
        else:
            lat, lon = citiesCoord[city]
            api_key = "28442b403d7c53f376bc6da1aae7fabb"
            url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

            response = requests.get(url)
            data = json.loads(response.text)["current"]

            temp = data["temp"]
            temperatureEmoji = getTempEmoji(temp)

            print(data)

            sr   = data["sunrise"]
            ss   = data["sunset"]

            sunrise = datetime.utcfromtimestamp(sr).strftime('%H:%M')
            sunset  = datetime.utcfromtimestamp(ss).strftime('%H:%M')

            await ctx.send("Current weather in {city}: {temp} °C {temoji} with a sunrise :sunrise: at {sunrise} and a sunset :city_sunset: at {sunset}"
                .format(city = city, temp = temp, temoji = temperatureEmoji, sunrise = sunrise, sunset = sunset))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global nr
    if message.author == client.user:
        return
    if message.author.id == 369108820313636865:
        print('test')
        await message.channel.send(random.choice(bullyMagnet))

    if message.channel.id == 400674062004781056:
        await message.channel.send('Pai si tu crezi ca esti amuzant ')

    if f'<@!{241955978466164737}>' in message.content:
        await message.channel.send('Ce vrei ma cu terminatul ala')

    if 'gusi' in message.content.lower():
        await message.channel.send('Mevic?')
    await client.process_commands(message)

#aquire config data
f = open("key.config","r")
key = f.readline()

#helper functions

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

#run bot
client.run(key)
