import discord
from discord.ext import commands
import os

# --- قسم الـ Flask (عشان ريندر ما يطفي البوت) ---
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
    return "I am alive"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# تشغيل السيرفر الصغير
keep_alive()
# ----------------------------------------------

# التوكن تبعك
TOKEN = 'MTQ5NzyXMDgXNzQxNDM2NTIxNA.GUqSN1.u4GcH_K1pXCEwlgPGmrJCfcLvTA_JKUQmysD2w'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'---------------------------------')
    print(f'تم تشغيل البوت بنجاح يا راشد: {bot.user}')
    print(f'---------------------------------')

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

# حط هون أوامر الرتب اللي عملناها قبل
@bot.command()
async def setup_roles(ctx):
    await ctx.send("أهلاً بك! البوت جاهز لإعطاء الرتب.")

bot.run(TOKEN)
