import discord
from discord.ext import commands

bot = commands.Bot()

TOKEN = ''
REQUIRED_ROLE_ID = 1237895655641448488

async def has_required_role(member):
    return any(role.id == REQUIRED_ROLE_ID for role in member.roles)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.upper() == 'SENDBOT':
        if await has_required_role(message.author):
            try:
                await message.author.send('You have been sent a message by the bot!')
            except discord.Forbidden:
                await message.channel.send('I do not have permission to DM you.')
            except discord.HTTPException as e:
                await message.channel.send(f'Error sending DM: {e.text}')
        else:
            await message.channel.send('You do not have the required role to receive a DM.')

bot.run(TOKEN)