import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # jeśli chcesz czytać treść wiadomości

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user}")

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
