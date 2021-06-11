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
  print(args)
  for arg in args:
    command += arg
  print(command)
  if command == "CAD":
    await ctx.channel.send('Here is the link to the CAD: https://ftc8404-ultimate-goal-robot-360.netlify.app/')
  if command == "PALS":
    await ctx.channel.send('Here is the link to the PALS homepage: https://pals.quixilver8404.org/')
  if command == "matchscouting":
    await ctx.channel.send('Here is the link to the PALS match scouting page: https://pals.quixilver8404.org/match-scouting')


keep_alive()
bot.run(os.environ['TOKEN'])