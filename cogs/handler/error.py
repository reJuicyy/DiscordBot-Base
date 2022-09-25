import discord
from discord.ext import commands
from data.cogs import __cogs__


class ErrorHandler(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        ignore_error = (commands.CommandNotFound, commands.UserInputError)

        if isinstance(error, ignore_error):
            return
        elif isinstance(error, commands.CommandOnCooldown):
            return await ctx.send(f"On Cooldown: {error.retry_after:.2f}")
        elif isinstance(error, commands.NoPrivateMessage):
            return await ctx.author.send(f"?")
        elif isinstance(error, commands.MissingPermissions):
            return await ctx.send(f"No permissions {ctx.command:.2f}")

def setup(bot):
    bot.add_cog(ErrorHandler(bot))