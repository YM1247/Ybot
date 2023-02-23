import discord
from discord.ext import commands
import os 
from dotenv import load_dotenv

load_dotenv() 
bot = commands.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

for cog in os.listdir('./cogs'):
    if cog.endswith('.py'):
        bot.load_extension(f'cogs.{cog[:-3]}')
        print(f'已加載{cog}')

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))