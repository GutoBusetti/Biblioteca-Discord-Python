import discord
from discord.ext import commands

client = commands.Bot(command_prefix='PREFIX')

@client.event
async def on_ready():
  print('Olá mundo')
  
@client.command()
async def ola(ctx):
  await ctx.send(f'Olá {ctx.author.mention}')

client.run('TOKEN DO BOT') 
