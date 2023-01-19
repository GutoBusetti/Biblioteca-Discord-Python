import disnake
from disnake.ext import commands

client = commands.Bot()

class Menu(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None


    @disnake.ui.button(label='Mensagem', style=disnake.ButtonStyle.red)
    async def menu1(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        await interaction.response.send_message('Você clicou em mim') 

    @disnake.ui.button(label='Edite', style=disnake.ButtonStyle.blurple)
    async def menu2(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        embed = disnake.Embed(
            description=f'mensagem editada com sucesso'
        )
        await interaction.response.edit_message(embed=embed) 

@client.slash_command(name='buttons', description='Botão com slash commands man.')
async def buttons(inter):
    if inter.author.id == 819183411142328370:
     view = Menu()
     embed = disnake.Embed(
        description=f'Click no botão vermelho para tag <@&1064027317262893137>\n CLick no botão verde para tag <@&1064027127357395034>',
        color=cor
     )
     view.add_item(disnake.ui.Button(label='url', style=disnake.ButtonStyle.link, url='https://m3dev.online'))
     await inter.response.send_message(embed=embed, view=view)
client.run('TOKEN')
