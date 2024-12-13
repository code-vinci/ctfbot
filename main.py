from discord.ext import commands
import discord
import os

TOKEN = os.getenv("DISCORD_TOKEN")

class CodeVinciBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix='/', intents=intents)

    async def setup_hook(self):
        for filename in os.listdir('commands'):
            if filename.endswith('.py'):
                await self.load_extension(f'commands.{filename[:-3]}')
        await self.tree.sync()

bot = CodeVinciBot()

@bot.event
async def on_ready():
    print(f'Bot is ready...')

bot.run(TOKEN)