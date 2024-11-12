import os
import discord
from discord.ext import commands

from dotenv import load_dotenv

# Create an intents object and enable the intents your bot needs
intents = discord.Intents.default()  # This enables the default intents
intents.message_content = True       # Enable access to message contentload_dotenv()
intents.presences = True
intents.members =True

TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name='pussyboy')
async def pussyboy(ctx):
    await ctx.send('Hello, Pussyboy!')

bot.run(TOKEN)
