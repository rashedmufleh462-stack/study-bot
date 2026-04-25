import discord
from discord.ext import commands
import os

# سحب التوكن من Render (Environment Variables)
TOKEN = os.getenv("DISCORD_TOKEN")

# إعداد البوت
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# لما البوت يشتغل
@bot.event
async def on_ready():
    print('---------------------------------')
    print(f'تم تشغيل البوت بنجاح يا راشد: {bot.user}')
    print('---------------------------------')

# أمر تجربة
@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

# أمر إعداد رتب (تجريبي)
@bot.command()
async def setup_roles(ctx):
    await ctx.send("أهلاً بك! البوت جاهز لإعطاء الرتب.")

# تشغيل البوت
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ خطأ: تأكد أنك حاط DISCORD_TOKEN في Render")
