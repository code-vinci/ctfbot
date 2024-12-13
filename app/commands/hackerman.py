import discord
from discord.ext import commands

class HackerMan(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name='hackerman', description='fancy Hackerman')
    async def create(self, interaction: discord.Interaction):
        await interaction.response.send_message("https://media.giphy.com/media/MM0Jrc8BHKx3y/giphy.gif", ephemeral=True)

async def setup(bot):
    await bot.add_cog(HackerMan(bot))