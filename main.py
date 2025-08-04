import discord
from discord.ext import commands
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Baza danych SQLite
def init_db():
    conn = sqlite3.connect("economy.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            cash INTEGER DEFAULT 0,
            bank INTEGER DEFAULT 0,
            reputation INTEGER DEFAULT 0,
            last_work REAL DEFAULT 0,
            last_crime REAL DEFAULT 0,
            last_slut REAL DEFAULT 0,
            jailed_until REAL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

@bot.event
async def on_ready():
    init_db()
    print(f"Bot gotowy jako {bot.user}")

# Komenda testowa
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Tu będą dodawane kolejne komendy, np. !work, !crime, !balance itd.

bot.run(TOKEN)
