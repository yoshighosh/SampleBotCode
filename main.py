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
async def get(ctx, *args):
  command = ""
  for arg in args:
    command += arg
  if command == "CAD":
    await ctx.channel.send('Here is the link to the CAD: https://ftc8404-ultimate-goal-robot-360.netlify.app/')
  elif command == "PALS":
    await ctx.channel.send('Here is the link to the PALS homepage: https://pals.quixilver8404.org/')
  elif command == "matchscouting":
    await ctx.channel.send('Here is the link to the PALS match scouting page: https://pals.quixilver8404.org/match-scouting')
  elif command == "pregamescouting":
    await ctx.channel.send('Here is the link to the PALS pregame scouting page: https://pals.quixilver8404.org/pre-game-scouting')
  elif command == "competitionoverview":
    await ctx.channel.send('Here is the link to the PALS competition overview: https://pals.quixilver8404.org/competition-overview')


keep_alive()
bot.run(os.environ['TOKEN'])