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

@bot.command()
async def get(ctx, arg):
  if arg == "CAD":
     await ctx.channel.send('Here is the link to the CAD: https://ftc8404-ultimate-goal-robot-360.netlify.app/')
  if arg == "PALS":
     await ctx.channel.send('Here is the link to the PALS homepage: https://pals.quixilver8404.org/')


keep_alive()
bot.run(os.environ['TOKEN'])