from discord.ext import commands
from data.cogs import __cogs__


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def cog_check(self, ctx):
        return await ctx.bot.is_owner(ctx.author)
    
    @commands.command(aliases=["get_cogs"], description="", usage=f"", hidden=True)
    async def cogs(self, ctx):
        await ctx.send(__cogs__)
    
    @commands.command(aliases=["load"], description="", usage=f"", hidden=True) 
    async def load_cog(self, ctx, cog):
        try:
            self.bot.load_extension(f'cogs.{cog}')
        except Exception as err:
            print(f"{cog} couldn't be loaded")
            raise err
        else:
            await ctx.send(f"{cog}: Successfully loaded")
            
    @commands.command(aliases=["unload"], description="", usage=f"", hidden=True) 
    async def unload_cog(self, ctx, cog):
        try:
            self.bot.unload_extension(f'cogs.{cog}')
        except Exception as err:
            print(f"{cog} couldn't be loaded")
            raise err
        else:
            await ctx.send(f"{cog}: Successfully unloaded")
            
    @commands.command(aliases=["reload"], description="", usage=f"", hidden=True)
    async def reload_cog(self, ctx, cog):
        try:
            self.bot.unload_extension(f'cogs.{cog}')
            self.bot.load_extension(f'cogs.{cog}')
        except Exception as err:
            print(f"'{cog}: couldn't be reloaded")
            raise err
        else:
            await ctx.send(f'{cog} : Successfully reloaded')
    
    @commands.command(aliases=["quit"], description="", usage=f"", hidden = True)
    async def close(self, ctx):
        await self.bot.close()
        print("Bot closed")


def setup(bot):
    bot.add_cog(Admin(bot))