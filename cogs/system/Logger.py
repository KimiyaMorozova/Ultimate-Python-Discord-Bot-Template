import discord
from discord.ext import commands 
import logging
from logging.handlers import RotatingFileHandler
from logging import handlers
import sys
import os

cwd = os.getcwd() #Get Current Dictonary


class Logger (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    LOGFILE=f"{cwd}/Log.txt"            #Log File
    log = logging.getLogger('')
    log.setLevel(logging.INFO)
    format = logging.Formatter("[%(asctime)s]-[%(name)s]-[%(levelname)s] - %(message)s")

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(format)
    log.addHandler(ch)

    fh = handlers.RotatingFileHandler(LOGFILE, maxBytes=(1048576*5), backupCount=7)
    fh.setFormatter(format)
    log.addHandler(fh)


def setup(bot):
    bot.add_cog(Logger(bot))    #Add the Logger Class to the Bot 