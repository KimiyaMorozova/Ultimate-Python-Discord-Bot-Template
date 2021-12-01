import discord
from discord.ext import commands 
import time
import asyncio


class example_command_cog (commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command(name="ping")                                          #name = how the command is called. #!No spaces!# 
    async def _ping(self, ctx):                                             #Defines Arguments  #!self is always first and there
        before = time.monotonic()                                           #Starts the timer
        message = await ctx.send("Pong! :ping_pong:")                       #Sends the message 
        ping = (time.monotonic() - before) * 1000                           #Counts the time that the client used to send the message and mulitplies it with 1000
        await message.edit(content=f"Pong! :ping_pong:  `{int(ping)}ms` ")  #Edits the message with the ping of the Server



    @commands.command(name="help")
    async def _help(self, ctx):
        await ctx.send("Help Command: \n-ping : Pong")



def setup(bot):
    bot.add_cog(example_command_cog(bot))