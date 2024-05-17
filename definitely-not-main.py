import discord, os
from pathlib import Path
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)  # Pass the intents parameter when creating the client

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

DS_TOKEN = os.environ['DS_TOKEN']



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):


    channel=message.channel
    reply_reference = message.reference or message.to_reference()
    print(channel)
    print(reply_reference)
    
    if message.author == client.user:
        return

    if 'raro' in message.content:
        
        await message.add_reaction('🤔')

        #await message.channel.send('no deberia pasar', reference=reply_reference)

    return

#hacer votacion oculta par kickear del SV a un usuario X con conteo de un keyword, que sume y reste y podamos consultar que tan cerca estamos.

#welp
client.run(DS_TOKEN)
