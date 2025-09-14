import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"✅ Zalogowano jako {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)
