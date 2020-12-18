import requests
import json
import discord
import random
from discord.ext import commands
from datetime import datetime

client = commands.Bot(command_prefix = '$')
bullyMagnet = ['De ce incerci?', 'Ba ?','Voi il vedeti pe asta ba @everyone', 'Iesi acasa', 'Iesi', 'Nu te-ai futut cu Andone nu?']
imgurCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
@client.command("weather")
async def _weather(ctx, args=""):
    if len(args.split()) != 1:
        await ctx.send("Weather command excepts only one argument!:grimacing:")
    else:
        location = args.lower()

        #geocoding
        url_geo = "https://maps.googleapis.com/maps/api/geocode/json?address={addr}+Mountain+View,+CA&key={key}".format(addr = location, key = geo_key)

        response = requests.get(url_geo)
        print(json.loads(response.text))



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def image(ctx):
    chosen_image = get_imgur_url()
    embed = discord.Embed(color=0xff69b4)
    embed.set_image(url = chosen_image)
    print(chosen_image)
    await ctx.send(embed = embed)

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
config = open("key.config","r")
discord_key = config.readline()
weather_key = config.readline()
geo_key = config.readline()
config.close()

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


def get_imgur_url():
    imgur_url = "http://i.imgur.com/"
    ext = ".jpg"
    code = ""

    for _ in range(0, 5):
        code += random.choice(imgurCharacters)

    full_url = imgur_url + code + ext
    return full_url


#run bot
client.run(discord_key)
