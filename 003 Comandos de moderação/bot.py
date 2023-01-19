import discord
from discord.ext import commands

client = commands.Bot(commabnd_prefix='Prefix')

@client.event
async def on_ready():
  print('Olá mundo')
  
@client.command()
async def kick(ctx, membro  : discord.Member, *, motivo=''):
  canal = client.get_channel(ID DO CANAL)
  msg = f'{ctx.author.mention} expulsou {membro.mention} pelo motivo: {motivo}'
  await membro.kick()
  await canal.send(msg)
  
@client.command()
async def ban(ctx, membro  : discord.Member, *, motivo=''):
  canal = client.get_channel(ID DO CANAL)
  msg = f'{ctx.author.mention} baniu {membro.mention} pelo motivo: {motivo}'
  await membro.ban()
  await canal.send(msg)
  

@client.slash_command(name='unban', description='Desbloquei um usuário bloquado.')
async def unban(inter, member : disnake.User, motivo=''):
         await inter.send('Mencione um motivo para poder desbanir o usuário')
        membro = await client.fetch_user(user_id=member.id)
        try:
            await inter.guild.unban(membro)
            await inter.send(f'{inter.author.mention} desbaniu {member.mention}, motivo: {motivo}')
        except:
            await inter.send('Erro ao desbanir membro.')
            
  
 client.run('TOKEN')
