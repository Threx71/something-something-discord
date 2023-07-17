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
    if message.author == client.user:
        return

    if 'raro' in message.content:
        
        await message.add_reaction('🤔')
        
    return

async def on_voice_state_update(member, before, after):
    # Check if the member is the specific user and the voice channel is the specific channel
    if member.id == 175690952961294336 and after.channel.id == 1117264119939219488:
        
        await member.guild.system_channel.send(f'{member.name} has joined {after.channel.name}!')

#welp
client.run(DS_TOKEN)