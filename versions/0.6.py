import discord										#Luna v0.6
import asyncio										#12/27/2017
from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime

Client = discord.Client()
bot_prefix= "+"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(game=discord.Game(name='+help'))

@asyncio.coroutine
def gofast():

	path = '/Users/kawaiikiana/Documents/Luna/hotdog/timer.txt'
	cake = open(path, 'r')
	check = cake.read()
	check = check.replace('timer: ','')
	check = int(check)
	while check > 0:

		cake.close()
		cake = open(path, 'r')
		check = cake.read()
		check = check.replace('timer: ','')
		check = int(check)

		check = check - 1
		newline = 'timer: ' + str(check)
		cake2 = open(path, 'w')
		cake2.writelines(newline)
		cake2.close()
		yield from asyncio.sleep(1)
	if check == 0:
		readme = open('/Users/kawaiikiana/Documents/Luna/hotdog/readme.txt', 'w')
		newline = '```diff*-Timer up-*```'
		read = readme.write(newline)

		info = '/Users/kawaiikiana/Documents/Luna/hotdog/info.txt'
		read = open(info, 'r')
		read2 = read.readlines()
		chili = read2[0]
		chili = chili.replace('[','')
		chili = chili.replace(']','')
		chili = chili.replace('\n','')

		num, seller, item, sbid = chili.split(':')
		hbid = read2[1]
		hbid = hbid.replace('hbid: ','')
		buyer = read2[2]
		buyer = buyer.replace('name: ','')
		now = datetime.now()
		date = now.strftime('%Y-%m-%d at %I:%M %p')

		sbid = sbid.replace(',','')
		sbid = sbid.replace(' Kamas','')
		hbid = hbid.replace(',','')
		hbid = hbid.replace(' Kamas','')
		sbid = int(sbid)
		hbid = int(hbid)
		if sbid == hbid:
			color = 0xFF5132
		if hbid > sbid:
			color = 0x70D666
		sbid = '{:,}'.format(sbid)
		hbid = '{:,}'.format(hbid)
		sbid = str(sbid)
		hbid = str(hbid)
		sbid = sbid + ' Kamas'
		hbid = hbid + ' Kamas'
		server = client.get_server('257665487066890241')
		cake = server.get_member_named('%s' % (seller))

		em = discord.Embed(colour=color)
		em.set_author(name='%s' % (item), icon_url='https://discordapp.com/assets/d59493c473541bf5d036c56e996b152b.svg')
		em.set_thumbnail(url='https://discordapp.com/assets/53ef346458017da2062aca5c7955946b.svg')
		em.add_field(name='Seller', value='%s' % (seller), inline=False)
		em.add_field(name='Starting Bid', value='%s' % (sbid), inline=False)
		em.add_field(name='Buyer', value='%s' % (buyer), inline=False)
		em.add_field(name='Selling Price', value='%s' % (hbid), inline=False)
		em.set_footer(text="Auctioneer Luna | %s" % (date))
		yield from client.send_message(discord.Object(id='382026630018629632'), embed=em)
		yield from client.send_message(discord.Object(id='383754383550316545'), embed=em)
		yield from client.send_message(cake, embed=em)

		dbase = '/Users/kawaiikiana/Documents/Luna/hotdog/database.txt'
		hotdog = open(dbase, 'r')
		dlines = hotdog.readlines()
		dcheck = dlines[0]

		info = '/Users/kawaiikiana/Documents/Luna/hotdog/info.txt'
		cheeseit = open(info, 'r')
		ilines = cheeseit.readlines()
		icheck = ilines[0]

		chilidog = open(dbase, 'w')

		if icheck == dcheck:
			for line in dlines:
				if not line.startswith(dcheck):
					chilidog.write(line)

		loopG = asyncio.get_event_loop()
		loopG.run_until_complete(respond())
		loopG.close()

@client.event
async def respond():
	readme = open('/Users/kawaiikiana/Documents/Luna/hotdog/readme.txt', 'r')
	pasta = readme.readlines()
	response = pasta[0]
	response = response.replace('*','\n')
	gchannel = '382026630018629632'
	await client.send_message(discord.Object(id=gchannel), str(response))

@client.event  
async def on_message(message):
	message.content = message.content.lower()
	if message.content.startswith('+mod'):
		name = '{0.author.mention}/'.format(message)
		name = name.replace('!', '')
		name = name.replace('<', '')
		name = name.replace('>', '')
		print(name)

	if message.content.startswith('cake'):
		server = message.server
		cake = server.get_member_named('Bari#4122')
		response = '-slidin into yo dm- :octopus: :wink: <:cawwot:378350427726544896>'
		await client.send_message(cake, str(response))

	if message.content.startswith('+pm'):
		response = 'Sliding into yo DM like <:miya:373879762138955777>'
		print(message.author)
		await client.send_message(message.author, str(response))

	if message.content.startswith('hello'):
		name = str(message.author.name)
		response = 'Hi %s :octopus:' % (name)
		await client.send_message(message.channel, str(response))

	if message.content.startswith('+hotdog'):
		response = '-gives a hotdog-'
		await client.send_message(message.channel, str(response))

	if message.content.startswith('+ping'):
		response = 'Pong!'
		await client.send_message(message.channel, str(response))

	if message.content.startswith('+join'):
		message = await client.get_message(message.channel, message.id)
		await client.delete_message(message)	

		nope = 0
		for r in message.author.roles:
			if r.id == "383742154880581652":
				nope = 1
		if nope == 1:
			await client.send_message(message.channel, "You have already received the role.")
		if nope == 0:

			name = str(message.author.name)
			channelID = str(message.channel.id)
			if channelID == '383748160083984384':
				temp = discord.utils.get(message.server.roles,name='Auction Friend')
				await client.add_roles(message.author, temp)
				response = 'Welcome to the Auction House, %s!' % (name)
				await client.send_message(message.channel, str(response))	

			if '383748160083984384' not in channelID:
				await client.send_message(message.channel, "You must be in the #join channel.")

	if message.content.startswith('you have already received the role.') or message.content.startswith('you must be in the #join channel.'):
		ID = str(message.author.mention)
		if "375493563833909248" in ID:
			await asyncio.sleep(3)
			message = await client.get_message(message.channel, message.id)
			await client.delete_message(message)

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
		response += '+view\n'
		response += '	- shows only your listings on the\n\n'		
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

	if message.content.startswith('+view'):
		user = str(message.author)
		view = open('/Users/kawaiikiana/Documents/Luna/hotdog/database.txt', 'r')
		result = 'no'
		lines = view.readlines()
		response = '```\n'
		for line in lines:
			if user in line:
				response += line
				result = 'yes'
		response += '```\n'
		if 'yes' in result:
			await client.send_message(message.channel, str(response))
		if 'no' in result:
			response = '```\n'
			response += 'You have no listings.\n'
			response += '```'
			await client.send_message(message.channel, str(response))

	if message.content.startswith('+astart'):
		name = '{0.author.mention}/'.format(message)
		name = name.replace('!', '')
		name = name.replace('<', '')
		name = name.replace('>', '')

		path = '/Users/kawaiikiana/Documents/Luna/hotdog/mods.txt'
		temp = open(path, 'r')
		lines = temp.readlines()
		check = lines[0]

		path2 = '/Users/kawaiikiana/Documents/Luna/hotdog/database.txt'
		hotdog = open(path2, 'r')
		lines3 = hotdog.read()
		hotdog.close()
		hotdog2 = open(path2, 'r')
		allowed = 0

		if name in check:
			allowed = 1
			if lines3 == '':
				response = 'There are no items up for auction.'
				await client.send_message(message.channel, str(response))

			if not lines3 == '':
				lines2 = hotdog2.readlines()
				auction = lines2[0]
				number, user, item, price = auction.split(':')
				price = price.replace('\n','')
				path3 = '/Users/kawaiikiana/Documents/Luna/hotdog/info.txt'
				cheese = open(path3, 'w')
				newlines = auction
				newlines += 'hbid: %s\n' % (price)
				newlines += 'name: none\n'
				cheese.write(newlines)

				path4 = '/Users/kawaiikiana/Documents/Luna/hotdog/timer.txt'
				pickle = open(path4, 'w')
				newlines = 'timer: 15'
				pickle.write(newlines)

				response = '```\n'
				response += 'Auction %s\n\n' % (number)
				response += 'Item: %s\n' % (item)
				response += 'Starting bid: %s\n' % (price)
				response += 'Seller: %s\n' % (user)
				response += '```'
				await client.send_message(message.channel, str(response))

		if allowed == 0:
			response = 'You do not have permission to start an auction'
			await client.send_message(message.channel, str(response))
		if allowed == 1:
			if not lines3 == '':
				loopF = asyncio.get_event_loop()
				loopF.run_until_complete(gofast())
				loopF.close()

	if message.content.startswith('+bid'):
		path = '/Users/kawaiikiana/Documents/Luna/hotdog/timer.txt'
		cake = open(path, 'r')
		check = cake.read()
		check = check.replace('timer: ','')
		check = int(check)
		if check > 0:

			name = str(message.author)

			path = '/Users/kawaiikiana/Documents/Luna/hotdog/info.txt'
			temp = open(path, 'r')
			lines = temp.readlines()

			hbid = lines[1]
			hbid = hbid.replace('hbid: ','')
			hbid = hbid.replace(' Kamas','')
			hbid = hbid.replace(',','')
			hbid = int(hbid)

			hname = lines[2]
			hname = hname.replace('name: ','')
			hname = hname.replace('\n','')
			hname = str(hname)
			allowed = 1

			minbid = 10
			if hbid > 1000:
				minbid = 100
			if hbid > 10000:
				minbid = 1000
			if hbid > 100000:
				minbid = 10000
			if hbid > 1000000:
				minbid = 100000
			if hbid > 10000000:
				minbid = 1000000
			if hbid > 100000000:
				minbid = 10000000

			lowbid = hbid + minbid

			raw = message.content

			if name == hname:
				allowed = 0
				response = "You may not bid if you're the previous bidder"
				await client.send_message(message.channel, str(response))

			if allowed == 1:
				if message.content == '+bid':
					bid = lowbid
				if message.content.startswith('+bid '):
					trash, bid = raw.split(' ')
					bid = bid.replace(',','')
					bid = int(bid)

				if lowbid > bid:
					response = 'Sorry, your bid cannot be lower than the current high bid. The lowest amount needed to bid currently is %s.' % (lowbid)
					await client.send_message(message.channel, str(response))
				if lowbid <= bid:
					temp = open(path, 'w')
					bid = '{:,}'.format(bid)
					bid = str(bid)
					newline = 'hbid: ' + bid + ' Kamas' + '\n'

					newname = 'name: ' + name + '\n'

					for line in lines:
						if not line.startswith('hbid:'):
							temp.write(line)
						if line.startswith('hbid:'):
							temp.write(newline)	
					temp.close()
					temp = open(path, 'r')
					lines = temp.readlines()
					temp = open(path, 'w')
					for line in lines:
						if not line.startswith('name:'):
							temp.write(line)			
						if line.startswith('name:'):
							temp.write(newname)

					xelor = '/Users/kawaiikiana/Documents/Luna/hotdog/timer.txt'
					relish = open(xelor, 'w')
					newlines = 'timer: 15'
					relish.write(newlines)

					response = '%s has bid %s kamas!' % (name, bid)
					await client.send_message(message.channel, str(response))

		if check == 0:
			path = '/Users/kawaiikiana/Documents/Luna/hotdog/info.txt'
			temp = open(path, 'r')
			lines = temp.readlines()
			line = lines[0]
			trash, name, item, kama = line.split(':')
			item = item.replace('[','')
			item = item.replace(']','')
			item = str(item)
			response = 'Oops! Too late-- bidding for %s has ended.' % (item)
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