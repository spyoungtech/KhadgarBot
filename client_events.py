import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {}({})'.format(client.user.name, client.user.id))
    print('--------------------')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await client.send.message(message.channel, 'Pong!')


