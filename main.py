import discord
import os
import requests
import json
import random
from replit import db


#Solution for .env file import
from dotenv import load_dotenv

load_dotenv()       #The load_dotenv() function looks for any .env file present in the current directory. After finding it will load them for use in your project

#upto this

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "miserable", "depressing"]

starter_encouragements = ["Cheerup!", "I will be ok.", "Stay strong."]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('!inspire'):
        quote = get_quote()
        await message.channel.send(quote)
 
client.run(os.getenv('TOKEN'))
