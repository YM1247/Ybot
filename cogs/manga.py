import discord
from discord.ext import commands
from discord.ui import Button, View
from core.classes import cogExtension

class manga(cogExtension):
    @commands.slash_command(name = 'cum', description = '輸入番號，然後瘋狂射精!')
    async def cum(self, ctx, code):
        url = f'https://nhentai.net/g/{code}'
        button = Button(label = f'點此前往: {code}', style = discord.ButtonStyle.green, url = url)   
        view = View(button)
        await ctx.respond(view = view)

def setup(bot):
    bot.add_cog(manga(bot))