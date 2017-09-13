import discord

@client.event
async def on_ready():
    print('Logged in as {}({})'.format(client.user.name, client.user.id))
    print('--------------------')
