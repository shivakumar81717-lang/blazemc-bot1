import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is online! Logged in as {bot.user}')

@bot.command()
async def help(ctx):
    await ctx.send('🔥 BlazeMC Bot Online hai! Commands: !verify, !ip, !rules')

@bot.command()
async def ip(ctx):
    await ctx.send('🎮 BlazeMC IP: `play.blazemc.space` Port: `19132`')

@bot.command()
async def verify(ctx):
    role = discord.utils.get(ctx.guild.roles, name='Members')
    if not role:
        await ctx.send('Members role nahi mila!')
        return
    await ctx.author.add_roles(role)
    await ctx.send('✅ Verified! Ab tu BlazeMC member hai!')

@bot.command()
async def rules(ctx):
    await ctx.send('📜 Rules: 1. No Hack 2. No Spam 3. Respect Staff')

bot.run(os.getenv('DISCORD_TOKEN'))
