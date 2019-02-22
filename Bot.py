import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
	print('The bot is ready!')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.command()
async def ping():
		await bot.say('**_you pinged MeKitty~_**')
		await bot.say('You pinged me! UwU')
	
@bot.command()
async def slap():
		await bot.say('**_you slapped MeKitty~_**')
		await bot.say('Ouch!! Hey what was that for?!')

@bot.command()
async def hug():
		await bot.say('**_you hug MeKitty~_**')
		await bot.say('Awe, your so sweet!')
		
bot.run('NTM1ODI2NTczMzU4NTMwNTYx.D1DTXQ.x7lRjifKfTjiXkf9PxK1eH4SYVI')
