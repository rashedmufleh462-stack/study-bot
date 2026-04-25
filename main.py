import discord
from discord.ext import commands
import os

# سحب التوكن من Render
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

# تشغيل البوت مع كشف الأخطاء
if TOKEN:
    try:
        bot.run(TOKEN)
    except Exception as e:
        print("❌ في خطأ أثناء تشغيل البوت:")
        print(e)
else:
    print("❌ ما لقيت DISCORD_TOKEN! تأكد إنه موجود في Render")
