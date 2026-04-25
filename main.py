import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

# 1. إعداد سيرفر Flask الصغير (عشان ريندر يضل صاحي)
app = Flask('')

@app.route('/')
def home():
    return "I am alive"

def run():
    # ريندر بيستخدم بورت 10000 غالباً، بس 8080 بتشتغل كمان
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. تشغيل السيرفر قبل تشغيل البوت
keep_alive()

# 3. إعدادات البوت والتوكن
# التوكن بيسحبه من الـ Environment Variables في ريندر
TOKEN = os.environ.get('DISCORD_TOKEN')

# تفعيل الـ Intents بالكامل
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

@bot.command()
async def setup_roles(ctx):
    await ctx.send("أهلاً بك! البوت جاهز لإعطاء الرتب.")

# 4. تشغيل البوت
if TOKEN:
    bot.run(TOKEN)
else:
    print("خطأ: لم يتم العثور على DISCORD_TOKEN في إعدادات Render!")
