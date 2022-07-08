"""A Markov chain generator that can tweet random messages."""

import os
import sys
import discord
from random import choice

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'weather' in message.content:
        await message.channel.send("It's about 90 degres of get out of my face outside")
    if 'po' in message.content:
        await message.channel.send('Fuck off, bitch!')

client.run(os.environ['DISCORD_TOKEN'])
