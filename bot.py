import discord
from discord.ext import commands
import json

with open('setting.json', mode='r', encoding='utf8') as dfile:
    ddata=json.load(dfile)

bot=commands.Bot(command_prefix="[")

@bot.event
async def on_read():
    print(">> bot is online <<")

@bot.event

async def on_member_join(member):
    channel = bot.get_channel(687745243776417859)
    await channel.send(f'{member} join!')

async def on_member_remove(member):
    channel = bot.get_channel(687745243776417859)
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (毫秒)')

bot.run(ddata['Token'])