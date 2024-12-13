import discord
from discord.ext import commands

class CreateChallengeCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name='create_challenge', description='Add new text channel to discuss about challenge')
    @discord.app_commands.checks.has_permissions(administrator=True)
    async def create_challenge(self, interaction: discord.Interaction, challenge_name: str):
        guild = interaction.guild
        category = interaction.channel.category

        if category is None:
            await interaction.response.send_message("Questo comando deve essere eseguito all'interno di una categoria!", ephemeral=True)
            return

        if not any(role.name == category.name for role in guild.roles):
            await interaction.response.send_message("Questa categoria non sembra essere parte di una CTF!", ephemeral=True)
            return

        challenge_channel = await guild.create_text_channel(name=challenge_name, category=category)
        await challenge_channel.edit(sync_permissions=True)

        await interaction.response.send_message(f"Canale creato con successo!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(CreateChallengeCommand(bot))
