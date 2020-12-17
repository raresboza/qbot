import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

client = discord.Client()

nr = 0
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event


async def on_message(message):
    global nr
    if message.author == client.user:
        return

    if message.author.id == 267709057219952640:
        if nr == 0:
            nr+=1
            await message.channel.send("Taci. {}".format(message.author.mention))
        elif nr == 1:
            nr += 1
            await message.channel.send('De ce incerci?')
        elif nr == 2:
            nr += 1
            await message.channel.send('Ba ?')
        else:
            nr += 1
            await message.channel.send('eu nu mai incerc cu asta @everyone')

    if message.content.startswith('$'):
        await message.channel.send('Hello!')

    if 'gusi' in message.content.lower():
        await message.channel.send('Mevic?')

f = open("key.config","r")
key = f.read()

client.run(key)
