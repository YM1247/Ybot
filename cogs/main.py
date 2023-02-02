import discord
from discord.ext import commands
from core.classes import CogExtension

class Main(CogExtension):
    @commands.slash_command(name = 'ping', description = 'ping pong!')
    async def ping(self, ctx):
        await ctx.respond(f'Pong! {round(self.bot.latency*1000)}ms')

def setup(bot):
    bot.add_cog(Main(bot))