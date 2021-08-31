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

# def update_encouragements(encouraging_messages):
#     if "encouragements" in db.keys():
#         encouragements = db["encouragements"]
#         encouragements.append(encouraging_messages)
#         db["encouragements"] = encouragements

#     else:
#         db["encouragements"] = [encouraging_messages]

# def delete_encouragement(index):
#     encouragements = db["encouragements"]
#     if len(encouragements) > index:
#         del encouragements[index]
#         db["encouragements"] = encouragements

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

    # options = starter_encouragements
    # if "encouragements" in db.keys():
    #     options = options + db["encouragements"]

    # if msg.startswith("!new_enc"):
    #     encouraging_messages = msg.split("!new_enc ",1)[1]
    #     update_encouragements(encouraging_messages)
    #     await message.channel.send("New encouragement message added.")

    # if msg.startswith("!del_enc"):
    #     encouragments = []
    #     if "encouragements" in db.keys():
    #         index = (msg.split("!del_enc", 1)[1])
    #         delete_encouragement(index)
    #         encouragments = db["encouragements"]
    #         await message.channel.send(encouragments)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))
 
client.run(os.getenv('TOKEN'))
