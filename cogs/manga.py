import discord, webbrowser
from discord.ext import commands
from core.classes import cogExtension

class manga(cogExtension):
    @commands.slash_command(name = '番號', description = '輸入番號，然後瘋狂射精!')
    async def cum(self, ctx, code, type):
        if type == 'e':
            url = f'https://www.wnacg.org/photos-index-aid-{code}'
        elif type == 'j':
            url = f'https://18comic.org/album/{code}'
        else:
            url = f'https://nhentai.net/g/{code}'
        

        webbrowser.open(url)
        await ctx.respond(f'已成功開啟車號{code}!')

def setup(bot):
    bot.add_cog(manga(bot))