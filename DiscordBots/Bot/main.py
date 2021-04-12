import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_SECRET')

client = discord.Client()
guild = client.get_guild(829220109779730452)

@client.event
async def on_ready():
    print(f'{client.user} has connected to the Discord Server.')

client.run(TOKEN)

print('Test')
name = guild.name
print(f'Name of the Discord Server: {name}')