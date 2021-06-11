from keep_alive import keep_alive
import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="$")

@bot.command()
async def hello(ctx):
   await ctx.channel.send("Hello!")

keep_alive()
bot.run(os.environ['TOKEN'])