import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Wczytanie tokena z pliku .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Intents potrzebne do czytania wiadomości i członków
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Utworzenie bota
bot = commands.Bot(command_prefix="!", intents=intents)

# EVENT: bot gotowy
@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')

# EVENT: powtarzanie wiadomości gracza
@bot.event
async def on_message(message):
    # Ignorowanie własnych wiadomości bota
    if message.author == bot.user:
        return

    # Powtarzanie wszystkiego, co napisze gracz
    await message.channel.send(f"{message.author.name} napisał: {message.content}")

    # Pozwolenie na działanie komend
    await bot.process_commands(message)

# KOMENDA: ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# KOMENDA: powiedz
@bot.command()
async def powiedz(ctx, *, tekst):
    await ctx.send(tekst)

# Uruchomienie bota
bot.run(TOKEN)
