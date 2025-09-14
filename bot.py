import os
from discord.ext import commands
from dotenv import load_dotenv
import discord  # dodajemy import discord

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Tutaj definiujemy intents
intents = discord.Intents.default()
intents.message_content = True  # dzięki temu bot może odczytywać treść wiadomości

# Tworzymy bota z intents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Zalogowano jako {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)
