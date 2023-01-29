import discord
from discord.ext import commands
from core.classes import cogExtension

class about(cogExtension):
    @commands.slash_command(name = 'about', description = 'about Ybot')
    async def about(self, ctx):
        embed = discord.Embed(
            title = '關於Ybot',
            description = '一些Ybot的事(不重要)',
            color = discord.Colour.blurple()
        )
        embed.add_field(
            name = '什麼是Ybot?',
            value = 'Ybot是由無聊沒事幹的廢物程式菜雞YM所開發出的dc bot',
            inline = True
        )
        embed.add_field(
            name = 'Ybot可以幹嘛?',
            value = '其實也不能幹嘛，蠻廢的',
            inline = True
        )
        embed.set_author(name= 'Ybot')
        embed.set_image(url='https://i.imgur.com/ILPEG5J.jpeg')
    
        await ctx.respond(embed = embed)

def setup(bot):
    bot.add_cog(about(bot))