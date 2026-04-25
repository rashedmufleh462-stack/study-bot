import discord
from discord.ext import commands
import os

# التوكن من Render Environment Variables
TOKEN = os.getenv("DISCORD_TOKEN")

# إعداد الـ intents بشكل آمن (أفضل من all)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# إنشاء البوت
bot = commands.Bot(command_prefix='!', intents=intents)

# حدث تشغيل البوت
@bot.event
async def on_ready():
    print('---------------------------------')
    print(f'تم تشغيل البوت بنجاح: {bot.user}')
    print('---------------------------------')

# أمر اختبار
@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

# أمر تجريبي
@bot.command()
async def setup_roles(ctx):
    await ctx.send("أهلاً! البوت شغال وجاهز 👍")

# تشغيل البوت
if not TOKEN:
    raise ValueError("❌ DISCORD_TOKEN غير موجود في Render Environment Variables")

bot.run(TOKEN)
