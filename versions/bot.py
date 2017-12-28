import discord										#Luna - working version
import asyncio										#11/17/2017
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

#@client.command(pass_context=True)
#async def ping(ctx):
#    await client.say("Pong!")

#prints user's ID in the terminal
@client.event  
async def on_message(message):
	message.content = message.content.lower()
	if message.content.startswith('?mod'):
		name = '{0.author.mention}/'.format(message)
		name = name.replace('!', '')
		name = name.replace('<', '')
		name = name.replace('>', '')
		print(name)
#random hotdog response
	if message.content.startswith('?hotdog'):
		response = '-gives a hotdog-'
		await client.send_message(message.channel, str(response))
#ping pong response
	if message.content.startswith('ping'):
		response = 'Pong!'
		await client.send_message(message.channel, str(response))
#whether the user is on the modlist or not
	if message.content.startswith('?am'):

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
#adds a listing to the auction list
	if message.content.startswith('?Add:') or message.content.startswith('?add'):
		charname = str(message.author) #charname = Bari#4122
		path = '/Users/kawaiikiana/Documents/Luna/hotdog/read.txt'
		temp = open(path, 'r')
		lines = temp.readlines() #sets it to a list: temp.readlines()
		check = lines[0] #checks line 1 of read: which is auction: yes/no
		number = lines[2] #checks line 3 of read: number: #
		number = number.replace('number:','')
		number = int(number) #turns number into an integer
		number = number + 1 #adds 1 to the number
		number = str(number) #turns number back into a string
		hotdog2 = open(path, 'w')
		for line in lines: #checks all the lines in the list (read.txt)
			if 'number' not in line: #if number is not in the line, it rewrites the line the same as before
				hotdog2.write(line)
			if 'number' in line: #if number is in the line, it replaces it with number: #
				writeline = 'number:' + number
				hotdog2.write(writeline)

		number = 'a' + number
		if 'yes' in check: #checks if auction:yes 
			said = str(message.content)
			said = said.replace('?add:','') #removes ?add from the command
			item, price = said.split(':') #item and price are split by : in the command
			price = price.replace(',','') #removes the commas in the price
			price = int(price) #turns price into an integer
			price = '{:,}'.format(price) #puts commas into the price. aka 100000 = 100,000
			newline = '[' + number + ']' + ':' + '[' + charname + ']' + ':' + '[' + item + ']' + ':' + price + ' Kamas\n' #new format to be written in the auctionlist database
			path2 = '/Users/kawaiikiana/Documents/Luna/hotdog/database.txt'
			hotdog = open(path2, 'r')
			lines2 = hotdog.readlines()
			temp2 = open(path2, 'w')
			temp2.writelines(lines2)
			temp2.write(newline) #writes the reformatted listing in the database


			response = 'Item listed.\n'
			response += '{}'.format(newline)
			await client.send_message(message.channel, str(response))
		if 'no' in check: #if there is no auction (auction:no then it will respond that there is no auction)
			response = 'There is no auction, or listing submissions have been closed.'
			await client.send_message(message.channel, str(response))

	if message.content.startswith('?list') or message.content.startswith('?list'):
		path = '/Users/kawaiikiana/Documents/Luna/hotdog/read.txt'
		temp = open(path, 'r')
		lines = temp.readlines()
		check = lines[0]

		path2 = '/Users/kawaiikiana/Documents/Luna/hotdog/database.txt'
		hotdog = open(path2, 'r')
		lines2 = hotdog.readlines()
		if 'yes' in check: #if listing:yes, then it will show the database listing
			response = '```\n'
			response += '\n'.join(lines2)
			response += '```'
			response = response.replace(':',' ') #removes all : in the listings
			await client.send_message(message.channel, str(response))
		if 'no' in check: #if auction:no, listings will not be shown
			response = 'There is no auction.'
			await client.send_message(message.channel, str(response))

	if message.content.startswith('?remove '):

		name = '{0.author.mention}/'.format(message)
		name = name.replace('!', '')
		name = name.replace('<', '')
		name = name.replace('>', '') #finds the user's id

		said = str(message.content)
		said = said.replace('?Remove ','')
		said = said.replace('?remove ','') #removes the command from the text
		charname = str(message.author) #the user's discord tag


		path = '/Users/kawaiikiana/Documents/Luna/hotdog/mods.txt'
		temp = open(path, 'r')
		lines = temp.readlines()
		check = lines[0]

		path2 = '/Users/kawaiikiana/Documents/Luna/hotdog/database.txt'
		hotdog = open(path2, 'r')
		lines2 = hotdog.readlines()
		allowed = 0
		readline = '[' + said + ']' #adds the brackets
		for line in lines2:
			if line.startswith(readline): #finds the correct listing
				checkline = line
				trash, user, item, price = line.split(':') #splits the listing at the : into these four variables
				user = user.replace('[','') #removes all brackets
				user = user.replace(']','')
		if charname.startswith(user): #allows user to remove listing if they are the owner of the listing
			allowed = 1
		if name in check: #allows user to remove listing if they are in the mod list
			allowed = 1
		if allowed == 1: #if the user has permission, then the listing will be removed.
			hotdog3 = open(path2, 'w')
			readline = '[' + said + ']'
			removed = 0
			for line in lines2:
				if not line.startswith(readline):
					hotdog3.write(line)
				if line.startswith(readline):
					removed = 1
			if removed == 0: #if no listing removed
				response = 'Listing not found.'
			if removed == 1:
				response = 'Listing has been removed.'
		if allowed == 0:
			response = "You don't have permission."
		await client.send_message(message.channel, str(response))

	if message.content.startswith('?Help') or message.content.startswith('?help'):
		response = '```\n'
		response += '===Market Commands===\n\n'
		response += '?List -- shows you the list of items on the market\n\n'
		response += '?Add:<itemName>:<Price> -- adds an item to the market, remove the <>\n\n'
		response += '?Remove <id> -- removes an item from the market. Note: only works on items you listed\n'
		response += '```'
		await client.send_message(message.channel, str(response))

	if message.content.startswith('?search '):
		term = message.content.replace('?search ','')
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
"""hot diggity dog dogs
a cat ate my shoe
holey cheetos
wait this actually works im amazed"""

