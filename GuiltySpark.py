import discord
import os
import sys
sys.path.append(os.getcwd())
from config import *
from discord.ext import commands
import asyncio
from itertools import cycle



client = commands.Bot(command_prefix = '.')

status = ['In the Library', 'Killing Flood', 'Dodging Spartan Lasers']

async def change_status():
	await client.wait_until_ready()
	msgs = cycle(status)

	while not client.is_closed:
		current_status = next(msgs)
		await client.change_presence(game=discord.Game(name=current_status))
		await asyncio.sleep(60*60)

@client.event
async def on_ready():
	#await client.change_presence(game=discord.Game(name='In the Library'))
	print('Bot is ready.')


'''
@client.event
async def on_message(message):
	author = message.author
	content = message.content
	print('{}: {}'.format(author, content))
	await client.process_commands(message) #checks for command, because on_message overrides commands

@client.event
async def on_message_delete(message):
	author = message.author
	content = message.content
	channel = message.channel
	await client.send_message(channel, '{}: {}'.format(author, content))

@client.command()
async def echo(*args):
	output = ''
	for word in args:
		output += word
		output += ' '
	await client.say(output)

@client.command(pass_context=True)
async def clear(ctx, amount=5):
	channel = ctx.message.channel
	messages = []
	async for message in client.logs_from(channel, limit=int(amount)):
		messages.append(message)
	await client.delete_messages(messages)
	await client.say('Messages deleted')

@client.event
async def on_member_join(member):
	role = discord.utils.get(member.server.roles, name='Example Role')
	await client.add_roles(member, role)
'''

@client.command()
async def displayembed():
	em = discord.Embed(
		title = 'Title',
		description = 'This is a description',
		color = discord.Color.gold()
	)

	em.set_footer(text='End statement')
	em.set_image(url='')
	em.set_thumbnail(url='')
	em.set_author(name='Author Name', icon_url='')
	em.add_field(name='Field Name', value='Field Value', inline=True)

	await client.say(embed=em)

@client.command()
async def ping():
	await client.say('pong!')

@client.command()
async def flip():
	await client.say('(╯°□°）╯︵ ┻━┻')

@client.command()
async def unflip():
	await client.say('┬─┬ ノ( ゜-゜ノ)')

@client.command()
async def shrug():
	await client.say('¯\_(ツ)_/¯')

'''
@bot.command()
async def playtime(ctx, time_played: int):
    if os.path.exists(f'{ctx.author.id}'):
        with open(f'{ctx.author.id}', 'r') as f:
            user_dict = json.load(f)
    else:
        user_dict = {}
    if user_dict.get('playtime', False) is False:
        user_dict = {'playtime': {}}
    now = dt.datetime.now()
    key = f'{now.year}-{now.month}-{now.day}'
    current_playtime = user_dict['playtime'].get(key, 0)
    current_playtime += time_played
    user_dict['playtime'][key] = current_playtime
    with open(f'{ctx.author.id}', 'w') as f:
        json.dump(user_dict, f)
    await ctx.send(f"added {time_played} {ctx.author.mention}'s current_playtime. Total playtime is now {current_playtime}")
'''

client.loop.create_task(change_status())

#defined in config.py
client.run(TOKEN)


