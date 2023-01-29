import discord
from discord.ext import commands
from core.classes import cogExtension

class embed(cogExtension):
    @commands.slash_command(name = 'hi', description = 'hihihi')
    async def hi(self, ctx):
        embed = discord.Embed(
            title="My Amazing Embed",
            description="Embeds are super easy, barely an inconvenience.",
            color=discord.Colour.blurple())
        embed.add_field(
            name="A Normal Field", 
            value="A really nice field with some information.")
        embed.add_field(name="Inline Field 1", value="Inline Field 1", inline=True)
        embed.add_field(name="Inline Field 2", value="Inline Field 2", inline=True)
        embed.add_field(name="Inline Field 3", value="Inline Field 3", inline=True)

        embed.set_footer(text="Footer! No markdown here.") 
        embed.set_author(
            name="Pycord Team", 
            icon_url="https://example.com/link-to-my-image.png")
        embed.set_thumbnail(url="https://example.com/link-to-my-thumbnail.png")
        embed.set_image(url="https://example.com/link-to-my-banner.png")

        await ctx.respond("Hello! Here's a cool embed.", embed=embed)

def setup(bot):
    bot.add_cog(embed(bot))