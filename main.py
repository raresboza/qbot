import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(name='test')
async def _test(ctx, args):
    await ctx.send(args)
    print("Haha")

f = open("key.config","r")
key = f.readline()

nr = 0
@client.event
async def on_message(message):
    global nr
    if message.author == client.user:
        return

#bully-on
    if message.author.id == 369108820313636865:
        if nr == 0:
            nr += 1
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

    if message.channel.id == 400674062004781056 :
        await message.channel.send('Pai si tu crezi ca esti amuzant ')

    if f'<@!{241955978466164737}>' in message.content:
        await message.channel.send('Ce vrei ma cu terminatul ala')

#    if message.content.startswith('$'):
#        await message.channel.send('Hello!')

#faza
    if 'gusi' in message.content.lower():
        await message.channel.send('Mevic?')

client.run(key)
