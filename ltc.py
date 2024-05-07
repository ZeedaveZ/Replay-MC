import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='ltc')
@commands.cooldown(1, 5, commands.BucketType.user)  # 1 use per 5 seconds per user
async def ltc(ctx):
    try:
        await ctx.send('LQjF8b398pmDAjbRYxn4Sk26ucLPTYNNjS')
    except discord.Forbidden:
        await ctx.send('I don\'t have permission to send messages in this channel.')

@bot.command(name='help')
async def help(ctx):
    embed = discord.Embed(title='Help', description='Available commands:')
    embed.add_field(name='.ltc', value='Responds with LQjF8b398pmDAjbRYxn4Sk26ucLPTYNNjS', inline=False)
    await ctx.send(embed=embed)

bot.run(MTIzMzIwNDE2ODg5OTE3MDM1NQ.GiubEg.3a7lVMl6V8bNpvhDyegH3gAZosd574DhTKh7ZE)