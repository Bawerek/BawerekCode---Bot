import os
import discord
from discord.ext import commands

# Pobieranie tokena z ENV
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("Brak tokena! Ustaw zmienną środowiskową DISCORD_TOKEN.")

# Intents – wymagane w discord.py 2.x
intents = discord.Intents.default()
intents.message_content = True  # pozwala botowi czytać treść wiadomości

# Tworzenie bota
bot = commands.Bot(command_prefix="!", intents=intents)

# Po zalogowaniu
@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')

# Komenda powtarzająca wiadomość
@bot.command()
async def powtorz(ctx, *, wiadomosc):
    await ctx.send(wiadomosc)

# Komenda testowa
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Uruchomienie bota
bot.run(TOKEN)
