import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == 145957053825810432:
        await message.channel.send('Taci.')

    if message.content.startswith('$'):
        await message.channel.send('Hello!')

    if 'gusi' in message.content.lower():
        await message.channel.send('Mevic?')

f = open("key.config","r")
key = f.read()

client.run(key)
