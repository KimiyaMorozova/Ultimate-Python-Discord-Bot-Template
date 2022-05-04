import discord
from discord.ext import commands 
import time
import asyncio


class example_slashcommand_cog (commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @commands.slash_command(name="help")
    async def _help(self, ctx):
        await ctx.respond("Help Command: \n-ping : Pong")



def setup(bot):
    bot.add_cog(example_slashcommand_cog(bot))
