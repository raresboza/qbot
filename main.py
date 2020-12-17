import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '$')
bullyMagnet = ['De ce incerci?', 'Ba ?','Voi il vedeti pe asta ba @everyone', 'Iesi acasa', 'Iesi', 'Nu te-ai futut cu Andone nu?']

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

def get_imgur_url():
    imgur_url = "http://i.imgur.com/"
    ext = ".jpg"
    r1 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    r2 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    r3 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    r4 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    r5 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

    code = r1 + r2 + r3 + r4 + r5
    full_url = imgur_url + code + ext
    return full_url

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

#run bot
client.run(key)
