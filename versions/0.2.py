import discord										#Luna v0.2
import asyncio										#11/23/2017
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
bot_prefix= "?"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(game=discord.Game(name='?help'))

@client.event  
async def on_message(message):
	message.content = message.content.lower()
	if message.content.startswith('+mod'):
		name = '{0.author.mention}/'.format(message)
		name = name.replace('!', '')
		name = name.replace('<', '')
		name = name.replace('>', '')
		print(name)

	if message.content.startswith('+hotdog'):
		response = '-gives a hotdog-'
		await client.send_message(message.channel, str(response))

	if message.content.startswith('+ping'):
		response = 'Pong!'
		await client.send_message(message.channel, str(response))

	if message.content.startswith('+am'):

		name = '{0.author.mention}/'.format(message)
		name = name.replace('!', '')
		name = name.replace('<', '')
		name = name.replace('>', '')

		path = '/Users/kawaiikiana/Documents/Luna/hotdog/mods.txt'
		temp = open(path, 'r')
		lines = temp.readlines()
		check = lines[0]
		if name in check:
			response = 'Yes, you are a hotdog'
		if name not in check:
			response = 'No, you are not a hotdog >:('
		await client.send_message(message.channel, str(response))

	if message.content.startswith('+add:'):
		charname = str(message.author)
		path = '/Users/kawaiikiana/Documents/Luna/hotdog/read.txt'
		temp = open(path, 'r')
		lines = temp.readlines()
		check = lines[0]
		number = lines[2] 
		number = number.replace('number:','')
		number = int(number)
		number = number + 1
		number = str(number)
		hotdog2 = open(path, 'w')
		for line in lines:
			if 'number' not in line:
				hotdog2.write(line)
			if 'number' in line:
				writeline = 'number:' + number
				hotdog2.write(writeline)

		number = 'a' + number
		if 'yes' in check:
			said = str(message.content)
			said = said.replace('+add:','')
			item, price = said.split(':')
			price = price.replace(',','')
			price = int(price)
			price = '{:,}'.format(price)
			newline = '[' + number + ']' + ':' + '[' + charname + ']' + ':' + '[' + item + ']' + ':' + price + ' Kamas\n'
			path2 = '/Users/kawaiikiana/Documents/Luna/hotdog/database.txt'
			hotdog = open(path2, 'r')
			lines2 = hotdog.readlines()
			temp2 = open(path2, 'w')
			temp2.writelines(lines2)
			temp2.write(newline)


			response = 'Item listed.\n'
			response += '{}'.format(newline)
			await client.send_message(message.channel, str(response))
		if 'no' in check:
			response = 'There is no auction, or listing submissions have been closed.'
			await client.send_message(message.channel, str(response))

	if message.content.startswith('+list'):
		path = '/Users/kawaiikiana/Documents/Luna/hotdog/read.txt'
		temp = open(path, 'r')
		lines = temp.readlines()
		check = lines[0]

		path2 = '/Users/kawaiikiana/Documents/Luna/hotdog/database.txt'
		hotdog = open(path2, 'r')
		lines2 = hotdog.readlines()
		if 'yes' in check:
			response = '```\n'
			response += '\n'.join(lines2)
			response += '```'
			response = response.replace(':',' ')
			await client.send_message(message.channel, str(response))
		if 'no' in check:
			response = 'There is no auction.'
			await client.send_message(message.channel, str(response))

	if message.content.startswith('+remove '):

		name = '{0.author.mention}/'.format(message)
		name = name.replace('!', '')
		name = name.replace('<', '')
		name = name.replace('>', '')

		said = str(message.content)
		said = said.replace('+remove ','')
		charname = str(message.author)


		path = '/Users/kawaiikiana/Documents/Luna/hotdog/mods.txt'
		temp = open(path, 'r')
		lines = temp.readlines()
		check = lines[0]

		path2 = '/Users/kawaiikiana/Documents/Luna/hotdog/database.txt'
		hotdog = open(path2, 'r')
		lines2 = hotdog.readlines()
		allowed = 0
		readline = '[' + said + ']'
		for line in lines2:
			if line.startswith(readline):
				checkline = line
				trash, user, item, price = line.split(':')
				user = user.replace('[','') 
				user = user.replace(']','')
		if charname.startswith(user):
			allowed = 1
		if name in check:
			allowed = 1
		if allowed == 1:
			hotdog3 = open(path2, 'w')
			readline = '[' + said + ']'
			removed = 0
			for line in lines2:
				if not line.startswith(readline):
					hotdog3.write(line)
				if line.startswith(readline):
					removed = 1
			if removed == 0:
				response = 'Listing not found.'
			if removed == 1:
				response = 'Listing has been removed.'
		if allowed == 0:
			response = "You don't have permission."
		await client.send_message(message.channel, str(response))

	if message.content.startswith('+help'):
		response = '```diff\n'
		response += '=======[ Market Commands ]=======\n\n'
		response += '+list\n'
		response += '	- shows all items listed on the market.\n\n'
		response += '+add:[itemName]:[Price]\n'
		response += '	- adds an item to the market, remove the brackets [ ]\n\n'
		response += '+remove [id]\n'
		response += '	- removes an item from the market.\n'
		response += '	- note: only works on items you listed\n\n'
		response += '+search [term]\n'
		response += '	- lists any items on market that include the term\n'
		response += '```'
		await client.send_message(message.channel, str(response))

	if message.content.startswith('+othercommands'):
		response = '```diff\n'
		response += '=======[ Luna v0.2 Commands ]=======\n\n'
		response += '+hotdog\n'
		response += '	- gives a hotdog. serves no real purpose.\n\n'
		response += '+ping\n'
		response += '	- ping pong. also no purpose.\n\n'
		response += '+mod\n'
		response += '	- displays your user ID in the terminal.\n\n'
		response += '+am\n'
		response += '	- displays mod status.\n\n'
		response += "=======[ Updated: Nov 23 17 ]=======\n"
		response += '```'
		await client.send_message(message.channel, str(response))

	if message.content.startswith('+search '):
		term = message.content.replace('+search ','')
		print(term)
		term = str(term)
		temp = open('/Users/kawaiikiana/Documents/Luna/hotdog/database.txt', 'r')
		result = 'no'
		templines = temp.readlines()
		response = '```\n'
		for line in templines:
			line = line.lower()
			if term in line:
				response += line
				result = 'yes'
		response += '```\n'
		if 'yes' in result:
			await client.send_message(message.channel, str(response))
		if 'no' in result:
			response = '```\n'
			response += 'Listing not found.\n'
			response += '```'
			await client.send_message(message.channel, str(response))

	'''if message.content.startswith('?search '):
		term = message.content.replace('?search ','')
		print(term)
		term = str(term)
		temp = open('/Users/kawaiikiana/Documents/Luna/hotdog/database.txt', 'r')
		templines = temp.readlines()
		response = '```\n'
		for line in templines:
			line = line.lower()
			if term in line:
				response += line
		response += '```\n'
		await client.send_message(message.channel, str(response))'''

	'''if message.content.startswith('?search '):
		term = message.content.replace('?search ','')
		print(term)
		term = str(term)
		temp = open('/Users/kawaiikiana/Documents/Luna/hotdog/database.txt', 'r')
		result = 'no'
		templines = temp.readlines()
		for line in templines:
			line = line.lower()
			if term in line:
				result = 'yes'
				if 'yes' in result:
					response = '```\n'
					for line in templines:
						line = line.lower()
						if term in line:
							response += line
					response += '```\n'
					await client.send_message(message.channel, str(response))
				if 'no' in result:
					response = '```\n'
					response += 'Listing not found.\n'
					response += '```'
					await client.send_message(message.channel, str(response))'''
	

client.run("bot token")