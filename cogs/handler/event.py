import discord
import random
import configparser
from discord.ext import commands
from data.cogs import __cogs__


class EventHandler(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        config = configparser.ConfigParser()
        config.readfp(open(r'data/config.cfg'))
        greet_channel = config.get('GLOBAL', 'greet_channel')
        
        emoji = [':wink:', ':wave:', ':tada:']
        channel = self.bot.get_channel(int(greet_channel))
        guild = member.guild
        await channel.send(f"Willkommen bei {guild.name} {random.choice(emoji)}, {member.mention}")
        
        
def setup(bot):
    bot.add_cog(EventHandler(bot))