import discord
from discord.ext import commands
import random
from core.classes import CogExtension

class RandomPick(CogExtension):
    @commands.slash_command(name = '隨機數字', description = '隨機取值')
    async def randomNum(self, ctx, start: discord.Option(int), end: discord.Option(int)):
        ram = random.randint(int(start), int(end))
        await ctx.respond(f'隨機數字{start} ~ {end} => {ram}')

    @commands.slash_command(name = '隨機', description = '從輸入中隨機取值')
    async def random(self, ctx, input):
        mes = input.split(' ')
        ram = random.randint(0, len(mes)-1)
        await ctx.respond(f'隨機{mes} => {mes[ram]}')

    @commands.slash_command(name = '擲骰', description = '骰出指定顆數&面數的骰子')
    async def dice(self, ctx, 顆數: discord.Option(int), 面數: discord.Option(int)):
        result = list()
        for i in range(int(顆數)):
            result.append(random.randint(1, int(面數)))
        await ctx.respond(f'{顆數}d{面數}:{result} => {sum(result)}')

def setup(bot):
    bot.add_cog(RandomPick(bot))