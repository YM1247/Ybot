import discord
from discord.ext import commands
import random
from core.classes import CogExtension

class DeleteCh(CogExtension):
    @commands.slash_command(name = '刪除頻道', description = '非常危險的指令')
    async def deleteChannel(self, ctx):
        await ctx.channel.delete(reason = f'由{ctx.author}刪除頻道')

def setup(bot):
    bot.add_cog(DeleteCh(bot))