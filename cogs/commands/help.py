import discord
from discord.ext import commands


class HelpCommandMember(commands.HelpCommand):
    def __init__(self, **options):
        super().__init__(**options)
        
    async def send_bot_help(self, mapping): # !help
        embed=discord.Embed(title="Admin Commands", color=0xff0000)
        #embed.set_author(name="Help")
        #embed.add_field(name="commands:", value="", inline=False)
        #embed.set_footer(text="Page x/n x Timestamp")
        
        for cog in mapping:
            for idx, command in enumerate(cog.get_commands()):
                print(idx, command.name)
                embed.add_field(name=command.name)
    
    async def send_cog_help(self, cog):
        await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in cog.get_commands()]}')
    
    async def send_group_help(self, group):
        await self.get_destination().send(f'{group.name}: {[command.name for index, command in enumerate(group.commands)]}')

    async def send_command_help(self, command): # !help <command>
        await self.get_destination().send(command.name)

    async def send_error_message(self, error):
        return await super().send_error_message(error)