import discord
from discord.ui import Button, View
from discord.ext import commands
from core.classes import CogExtension

class ChSet(CogExtension):
    @commands.slash_command(description = 'setting private channel')
    async def set(self, ctx):
        button = Button(label = '點我開啟私人頻道', style = discord.ButtonStyle.green)
        guild = ctx.guild
        category = ctx.channel.category
        name = ctx.author
        overwrites = {
            name : discord.PermissionOverwrite(manage_channels = True)
        }

        async def button_callback():
            ch = await guild.create_text_channel(
                name = f'{str(name)[:-5]}的個人頻道',
                category = category,
                overwrites = overwrites
                )
            close_button = Button(label= '點我關閉此頻道', style = discord.ButtonStyle.red)
            
            async def close_button_callback():
                await ch.delete()
            
            close_button.callback = close_button_callback
            close_view = View(close_button)
            await ch.send(f'這裡是{str(name)[:-5]}的個人頻道!', view = close_view)

        button.callback = button_callback

        view = View(button)
        await ctx.respond(view = view)

def setup(bot):
    bot.add_cog(ChSet(bot))