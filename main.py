import discord
import configparser
import logging
from logging.handlers import RotatingFileHandler
from discord.ext import commands
from data.cogs import __cogs__
from cogs.commands.help import HelpCommandMember


logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = RotatingFileHandler(filename='logs/bot.log', maxBytes=1024 * 5, backupCount=2, encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


config = configparser.ConfigParser()
config.readfp(open(r'data/config.cfg'))
token = config.get('GLOBAL', 'token')
prefix = config.get('GLOBAL', 'prefix')


__version__ = "0.0.1"
bot = commands.Bot(command_prefix=prefix, help_command=HelpCommandMember())


@bot.event
async def on_ready():
    bot_info = await bot.application_info()
    
    print(f"[I] Owner: {bot_info.owner}")
    print(f"[I] Bot-Name: {bot.user.name}")
    print(f"[I] Bot-ID: {bot.user.id}")
    print(f"[I] Bot Version: {__version__}")
    
    for cog in __cogs__:
        try:
            bot.load_extension(f"cogs.{cog}")
        except Exception as e:
            print(f"[E] {cog} couldn't be loaded")
            raise e
        else:
            print(f"[S] {cog} successfully loaded")
    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Indeed, a wise choice."))
    

if __name__ == "__main__":
    bot.run(token)