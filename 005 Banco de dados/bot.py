import discord
import json
from discord.ext import commands

client = commabnds.Bot(command_prefix='Prefix')

@client.event
async def on_ready():
  print('Olá mundo')
  
  
  with open('config.js') as e: # armazenando com Json
    config = json.load(e)
    TOKEN = config['token']
  
  with open('token.txt','r') as archive:
    TOKEN = archive.read()
    
   
client.run('TOKEN')
