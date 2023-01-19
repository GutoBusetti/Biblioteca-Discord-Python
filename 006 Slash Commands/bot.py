import disnake  # para slash sugiro disnake/ mas também pode usar discord.py / pycord
from disnake.ext import commands

client = command.Bot()

@client.slash_command(name='teste', description='Testando...')
async def teste(inter)
  await inter.response.send_message(f'Olá {inter.author.mention}')
  
client.run('TOKEN')
