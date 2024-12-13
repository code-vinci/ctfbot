import discord
from discord.ext import commands

class CreateCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name='create', description='Creates a new CTF.')
    @discord.app_commands.checks.has_permissions(administrator=True)
    async def create(self, interaction: discord.Interaction, ctf_name: str):
        guild = interaction.guild

        role = await guild.create_role(name=ctf_name)

        category = await guild.create_category(ctf_name)
        overwrites_private = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False, connect=False),
            role: discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True)
        }
        overwrites_public = {
            guild.default_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            role: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        await category.edit(overwrites=overwrites_private)

        tc_registration = await guild.create_text_channel("registration", category=category)
        await tc_registration.edit(overwrites=overwrites_public)

        tc_general = await guild.create_text_channel("general", category=category)
        await tc_general.edit(sync_permissions=True)

        btn = discord.ui.Button(label="Registrati", style=discord.ButtonStyle.primary)
        btn.callback = lambda interact: self.manage_btn(interact, role)
        
        view = discord.ui.View()
        view.add_item(btn)

        await tc_registration.send("Clicca per partecipare a questa CTF.", view=view)

        await interaction.response.send_message("CTF Creata con successo!", ephemeral=True)

    async def manage_btn(self, interact: discord.Interaction, role: discord.Role):
        member = interact.user
        if role in member.roles:
            await interact.response.send_message("Hai già il ruolo!", ephemeral=True)
        else:
            await member.add_roles(role)
            await interact.response.send_message("Ti sei registrato con successo!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(CreateCommand(bot))
