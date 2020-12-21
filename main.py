import requests
import discord
import hashlib
import random
import helper_functions as func
import json
from discord.ext import commands
from geopy.geocoders import Nominatim
from pyowm.owm import OWM

client = commands.Bot(command_prefix = '$')
bullyMagnet = ['De ce incerci?', 'Ba ?','Voi il vedeti pe asta ba @everyone', 'Iesi acasa', 'Iesi', 'Nu te-ai futut cu Andone nu?']

imgurNotFound = '9b5936f4006146e4e1e9025b474c02863c0b5614132ad40db4b925a10e8bfbb9'
imgurSecondError = '9712f09e69148642e9fe1f98d9fbef4eb1a130ec4b29240c04f98333ebf94635'

@client.command("weather")
async def _weather(ctx, address=""):
    await ctx.send("This feature is currently unavailable :(")
    #geocodingz
    location = geolocator.geocode(address)

    print(location.address)
    print((location.latitude, location.longitude))

    #open weather map
    one_call = mgr.one_call(lat = location.latitude,lon = location.longitude)

    #data = json.loads(response.text)

    #await ctx.send(func.process_weather_data(data, location))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def image(ctx):
    while True:
        chosen_image = func.get_imgur_url()
        print(chosen_image)

        response = requests.get(chosen_image, stream=True)
        m = hashlib.sha256()
        m.update(response.content)

        if m.hexdigest() != imgurNotFound and m.hexdigest() != imgurSecondError:
            print(m.hexdigest())
            print(imgurNotFound)
            break

    """
    If you want to download the picture:
        if response.status_code == 200:
        with open('img.png', 'wb') as f:
            for chunk in response:
                f.write(chunk)
    """

    embed = discord.Embed(color=0xff69b4)
    embed.set_image(url=chosen_image)
    await ctx.send(embed=embed)

@client.event
async def on_message(message):
    global nr
    if message.author == client.user:
        return
    if message.author.id == 369108820313636865:
        print('test')
        await message.channel.send(random.choice(bullyMagnet))

    if message.channel.id == 400674062004781056:
        await message.channel.send('Pai si tu crezi ca esti amuzant?')

    if f'<@!{241955978466164737}>' in message.content:
        await message.channel.send('Ce vrei ma cu terminatul ala')

    if 'gusi' in message.content.lower():
        await message.channel.send('Mevic?')
    await client.process_commands(message)

#aquire config data
config = open("key.config","r")
discord_key = config.readline()
weather_key = config.readline()
config.close()

#run bot
geolocator = Nominatim(user_agent="discord-bot")
print(weather_key)
owm = OWM(weather_key)
mgr = owm.weather_manager()

client.run(discord_key)
