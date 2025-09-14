import os
import discord
from discord.ext import commands

# Pobieranie tokena z zmiennych środowiskowych
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("Brak tokena! Ustaw zmienną środowiskową DISCORD_TOKEN.")

# Prefix komend
bot = commands.Bot(command_prefix="!")

# Po zalogowaniu
@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')

# Powtarzanie wiadomości gracza
@bot.command()
async def powtorz(ctx, *, wiadomosc):
    await ctx.send(wiadomosc)

# Prosta komenda testowa
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Uruchomienie bota
bot.run(TOKEN)
