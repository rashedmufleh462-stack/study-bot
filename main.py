import discord
from discord.ext import commands
from discord.ui import Button, View

TOKEN = 'MTQ5NzYxMDgxNzQxNDM2NTIxNA.GUqSNl.u4GcH_K1pXCEwlgPGmrJCfcLvTA_JKUQmysD2w'
WELCOME_CHANNEL_ID = 1487891330532249611 # قناة الترحيب

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# IDs الرتب
GRADE_ROLES = {
    "grade_10": 1497616895619371129,
    "grade_11": 1497616958114365663,
    "grade_12": 1497617031388725503
}

class GradeView(View):
    def __init__(self):
        super().__init__(timeout=None)

    async def check_and_assign(self, interaction: discord.Interaction, role_id: int):
        await interaction.response.defer(ephemeral=True)
        
        user_role_ids = [r.id for r in interaction.user.roles]
        if any(rid in GRADE_ROLES.values() for rid in user_role_ids):
            await interaction.followup.send("يا بطل، معك رتبة أصلاً! لا يمكنك أخذ رتبة ثانية. ⚠️", ephemeral=True)
            return

        role = interaction.guild.get_role(role_id)
        if role:
            try:
                await interaction.user.add_roles(role)
                await interaction.followup.send(f"تم إعطاؤك رتبة {role.name} بنجاح! ✅", ephemeral=True)
            except discord.Forbidden:
                await interaction.followup.send("مشكلة صلاحيات! ارفع رتبة البوت فوق رتب الصفوف. ❌", ephemeral=True)
        else:
            await interaction.followup.send("الرتبة غير موجودة! ❌", ephemeral=True)

    @discord.ui.button(label="صف عاشر", style=discord.ButtonStyle.primary, custom_id="btn_10")
    async def grade_10(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.check_and_assign(interaction, GRADE_ROLES["grade_10"])

    @discord.ui.button(label="أول ثانوي", style=discord.ButtonStyle.success, custom_id="btn_11")
    async def grade_11(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.check_and_assign(interaction, GRADE_ROLES["grade_11"])

    @discord.ui.button(label="توجيهي", style=discord.ButtonStyle.danger, custom_id="btn_12")
    async def grade_12(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.check_and_assign(interaction, GRADE_ROLES["grade_12"])

@bot.event
async def on_ready():
    print(f'---------------------------------')
    print(f'البوت {bot.user} جاهز للعمل!')
    print(f'---------------------------------')

# الترحيب التلقائي بالعنوان الجديد
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title="Welcome to the Study Community!",
            description=f"Welcome {member.mention}\nPlease choose your grade to get access:",
            color=discord.Color.blue()
        )
        await channel.send(embed=embed, view=GradeView())

# أمر الـ Setup اليدوي بالعنوان الجديد
@bot.command()
async def setup(ctx):
    embed = discord.Embed(
        title="Welcome to the Study Community!", 
        description="Choose your grade by clicking the buttons below:", 
        color=discord.Color.green()
    )
    await ctx.send(embed=embed, view=GradeView())

bot.run(TOKEN)