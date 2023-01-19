import discord # importações das libs usadas, aqui no caso a do Discord
fro discord.ext import commands

client = commands.Bot()

@client.event
async def on_ready():
  print('Olá mundo')
  
  client.run('Seu token') # token do bot
