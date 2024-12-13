import discord
from discord.ext import commands

class FlagCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name='flag', description="Marks the challenge as solved with a 🚩 emoji.")
    @discord.app_commands.checks.has_permissions(administrator=True)
    async def flag(self, interaction: discord.Interaction):
        channel = interaction.channel

        if not isinstance(channel, discord.TextChannel):
            await interaction.response.send_message("Questo comando può essere eseguito solo in un canale testuale.", ephemeral=True)
            return

        flag_emoji = "🚩" 
        if channel.name.startswith(flag_emoji):
            await interaction.response.send_message("Il canale ha già una bandierina nel nome!", ephemeral=True)
            return

        new_name = f"{flag_emoji}{channel.name}"
        await channel.edit(name=new_name)

        await interaction.response.send_message(f"Bandierina aggiunta al nome del canale: {new_name}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(FlagCommand(bot))
