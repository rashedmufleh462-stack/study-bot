import discord
from discord.ext import commands
from discord.ui import Button, View

# التوكن الخاص بك
TOKEN = 'MTQ5NzyXMDgXNzQxNDM2NTIxNA.GUqSN1.u4GcH_K1pXCEwlgPGmrJCfcLvTA_JKUQmysD2w'

# إعدادات البوت
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# رتب الصفوف (تأكد أن الأيدي صحيح)
GRADE_ROLES = {
    "grade_10": 1497616895619371129,
    "grade_11": 1497616958114365663,
    "grade_12": 1497617031388725503
}

@bot.event
async def on_ready():
    print(f'---------------------------------')
    print(f'تم تشغيل البوت بنجاح: {bot.user}')
    print(f'---------------------------------')

@bot.command()
async def setup_roles(ctx):
    """أمر لإنشاء أزرار الرتب"""
    view = View()
    
    btn10 = Button(label="الصف العاشر", style=discord.ButtonStyle.primary, custom_id="grade_10")
    btn11 = Button(label="الصف الحادي عشر", style=discord.ButtonStyle.success, custom_id="grade_11")
    btn12 = Button(label="الصف الثاني عشر", style=discord.ButtonStyle.danger, custom_id="grade_12")

    async def button_callback(interaction):
        role_id = GRADE_ROLES.get(interaction.data['custom_id'])
        role = interaction.guild.get_role(role_id)
        if role:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"تم إعطاؤك رتبة {role.name} بنجاح!", ephemeral=True)
        else:
            await interaction.response.send_message("خطأ: لم يتم العثور على الرتبة في السيرفر.", ephemeral=True)

    btn10.callback = button_callback
    btn11.callback = button_callback
    btn12.callback = button_callback

    view.add_item(btn10)
    view.add_item(btn11)
    view.add_item(btn12)

    await ctx.send("اختر صفك الدراسي للحصول على الرتبة:", view=view)

bot.run(TOKEN)
