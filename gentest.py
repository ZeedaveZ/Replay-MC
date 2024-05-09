import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.slash(name='send', description='Send a private message to the user.')
async def send(ctx):
    await ctx.author.send('Hello {}!'.format(ctx.author.display_name))
    await ctx.send('A private message has been sent to you.')

bot.run('BOT_TOKEN')
