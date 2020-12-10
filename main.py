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

    if message.content.startswith('$'):
        await message.channel.send('Hello!')

client.run("Nzg2NjUwNDUyNzE5Njk3OTQw.X9JfUw.w_44xWRgDLkdy0lPmFO8C8kqyuI")