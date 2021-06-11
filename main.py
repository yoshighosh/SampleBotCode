from keep_alive import keep_alive
import discord
import os
from discord.ext import commands
import Commands

bot = commands.Bot(command_prefix="$")

bot.remove_command('help')

@bot.command()
async def hello(ctx):
   await ctx.channel.send("Hello!")

@bot.command(name="help")
async def commands(ctx):
   await ctx.channel.send(Commands.commandList)


keep_alive()
bot.run(os.environ['TOKEN'])