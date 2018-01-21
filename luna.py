import discord                                      #Luna v0.6
import asyncio                                      #12/27/2017
import os
import aiohttp
import yaml
from PIL import Image
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

@client.event
async def on_message_delete(message):
    server = message.server.id
    path = '/Users/kawaiikiana/Documents/Luna/Servers/%s/read.txt' % (server)
    cake = open(path, 'r')
    check = cake.readlines()
    carrot = check[1]
    if 'yes' in carrot:
        delm = str(message.content)
        author = str(message.author) + ' (' + message.author.mention + ')'
        now = datetime.now()
        timestamp = str(now) + ' | ' + str(message.server.name)

        em = discord.Embed(description='%s' % (author), color=0xffc744)
        em.set_author(name='Deleted Message')
        em.add_field(name='Deleted Content', value='```%s```' % (delm), inline=False)
        em.set_footer(text='%s' % (timestamp))
        await client.send_message(discord.utils.get(message.server.channels, name='message-log'), embed=em)
        cake.close()

@client.event
async def on_message_edit(before, after):
    if before.author.bot:
        return
    path = '/Users/kawaiikiana/Documents/Luna/Servers/%s/read.txt' % (before.server.id)
    cake = open(path, 'r')
    check = cake.readlines()
    carrot = check[2]
    if 'yes' in carrot:
        author = str(before.author) + ' (' + before.author.mention + ')'
        newm = str(after.content)
        oldm = str(before.content)
        now = datetime.now()
        timestamp = str(now) + ' | ' + str(before.server.name)
        em = discord.Embed(description='%s' % (author), color=0xffc744)
        em.set_author(name='Editted Message')
        em.add_field(name='Original Content', value='```%s```' % (oldm), inline=False)
        em.add_field(name='Updated Content', value='```%s```' % (newm), inline=False)
        em.set_footer(text='%s' % (timestamp))
        await client.send_message(discord.utils.get(before.server.channels, name='message-log'), embed=em)

@client.event
async def on_server_join(server):
    print("Luna has joined the server [%s]!" % (server.name))
    folder = '/Users/kawaiikiana/Documents/Luna/Servers/%s' % (server.id)
    print(folder)
    if not os.path.exists(folder):
        os.makedirs(folder)
        if os.path.exists(folder):
            file1 = '/Users/kawaiikiana/Documents/Luna/Servers/%s/database.txt' % (server.id)
            file2 = '/Users/kawaiikiana/Documents/Luna/Servers/%s/read.txt' % (server.id)
            file3 = '/Users/kawaiikiana/Documents/Luna/Servers/%s/timer.txt' % (server.id)
            file4 = '/Users/kawaiikiana/Documents/Luna/Servers/%s/info.txt' % (server.id)
            file5 = '/Users/kawaiikiana/Documents/Luna/Servers/%s/mute.txt' % (server.id)
            hotdog = open(file1, 'w+')
            hotdog.close()
            chilidog = open(file2, 'w+')
            chilidog.write('auction:yes\nmessagedel:no\nmessageedit:no\ntimer:0\nnumber:1')
            chilidog.close()
            corndog = open(file3, 'w+')
            corndog.close()
            pizza = open(file4, 'w+')
            pizza.close()
            tunapoki = open(file5, 'w+')
            tunapoki.close()

@asyncio.coroutine
async def gofast(server, channel):

    path = '/Users/kawaiikiana/Documents/Luna/Servers/%s/timer.txt' % (server)
    cake = open(path, 'r')
    check = cake.read()
    check = check.replace('timer: ','')
    check = int(check)
    cake.close()
    
    while check > 0:
        
        cake = open(path, 'r')
        check = cake.read()
        check = check.replace('timer: ','')
        check = int(check)

        check = check - 1
        newline = 'timer: ' + str(check)
        cake2 = open(path, 'w')
        cake2.writelines(newline)
        cake2.close()
        await asyncio.sleep(1)

    if check == 0:

        newline = '```diff\n-Timer up-```'
        info = '/Users/kawaiikiana/Documents/Luna/Servers/%s/info.txt' % (server)
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
        aserver = client.get_server(server)
        cake = aserver.get_member_named('%s' % (seller))

        await client.send_message(discord.Object(id=channel), str(newline))

        em = discord.Embed(colour=color)
        em.set_author(name='%s' % (item), icon_url='https://discordapp.com/assets/d59493c473541bf5d036c56e996b152b.svg')
        em.set_thumbnail(url='https://discordapp.com/assets/53ef346458017da2062aca5c7955946b.svg')
        em.add_field(name='Seller', value='%s' % (seller), inline=False)
        em.add_field(name='Starting Bid', value='%s' % (sbid), inline=False)
        em.add_field(name='Buyer', value='%s' % (buyer), inline=False)
        em.add_field(name='Selling Price', value='%s' % (hbid), inline=False)
        em.set_footer(text="Auctioneer Luna | %s" % (date))
        await client.send_message(discord.utils.get(aserver.channels, name='archived-results'), embed=em) #send results in archive channel
        await client.send_message(discord.Object(id=channel), embed=em)
        await client.send_message(cake, embed=em)

        dbase = '/Users/kawaiikiana/Documents/Luna/Servers/%s/database.txt' % (server)
        hotdog = open(dbase, 'r')
        dlines = hotdog.readlines()
        dcheck = dlines[0]

        info = '/Users/kawaiikiana/Documents/Luna/Servers/%s/info.txt' % (server)
        cheeseit = open(info, 'r')
        ilines = cheeseit.readlines()
        icheck = ilines[0]

        chilidog = open(dbase, 'w')

        if icheck == dcheck:
            for line in dlines:
                if not line.startswith(dcheck):
                    chilidog.write(line)

@client.event  
async def on_message(message):
    if message.author.bot:
        return
    path = '/Users/kawaiikiana/Documents/Luna/Servers/%s/mute.txt' % (message.server.id)
    read = open(path, 'r')
    mango = read.readlines()
    author = str(message.author.id)
    for line in mango:
        if line.startswith(author):
            return    
    path = '/Users/kawaiikiana/Documents/Luna/Servers/%s/prefix.txt' % (message.server.id)
    if not os.path.exists(path):
        tunapoki = open(path, 'w+')
        tunapoki.write('+')
        tunapoki.close()
    cake = open(path, 'r')
    prefix = cake.read()
    cake.close()
    if message.content.startswith(str(prefix)):
        text = str(message.content)
        testing = text.replace(str(prefix),'')
        okay = testing.lower()
        await commands(command=okay, message=message)

@client.event
async def commands(command, message):
    
    if command.startswith('setprefix'):
        nprefix = command.replace('setprefix ','')
        path = '/Users/kawaiikiana/Documents/Luna/Servers/%s/prefix.txt' % (message.server.id)
        read = open(path, 'w')
        read.writelines(nprefix)
        read.close()

    if command.startswith('info'):
        embed=discord.Embed(title="Bot info", color=0xbf91ff)
        embed.set_author(name="Luna", url="https://discordbots.org/bot/375493563833909248", icon_url="https://cdn.discordapp.com/avatars/375493563833909248/a80f64785de7413405a41ebf28b248d1.png?size=1024")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/375493563833909248/a80f64785de7413405a41ebf28b248d1.png?size=1024")
        embed.add_field(name="ID", value="375493563833909248", inline=False)
        embed.add_field(name="Discord tag", value="Luna#0204", inline=False)
        embed.add_field(name="Description", value="I'm Luna! A Discord bot programmed to host auctions among other miscellaneous things. I'm currently in development, please check my support server for more information on my uptime and updates.", inline=False)
        embed.add_field(name="Library", value="discord.py", inline=True)
        embed.add_field(name="Prefix", value="insertprefix", inline=True)
        embed.add_field(name="Server Count", value="inserthere", inline=True)
        embed.add_field(name="Developer", value="Miya#0270", inline=True)
        embed.add_field(name="Links", value="[Invite Me](https://discordapp.com/api/oauth2/authorize?client_id=375493563833909248&permissions=0&scope=bot) - [Support Server](https://discord.gg/tJEm7Zp) - [Donate](https://www.patreon.com/miyami)", inline=False)
        await client.send_message(message.channel, embed=embed)

    if command.startswith('hello'):
        name = str(message.author.display_name)
        response = 'Hi %s :octopus:' % (name)
        await client.send_message(message.channel, str(response))

    if command.startswith('hotdog'):
        response = '-gives a hotdog-'
        await client.send_message(message.channel, str(response))

    if command.startswith('ping'):
        response = 'Pong!'
        await client.send_message(message.channel, str(response))

    if command.startswith('am'):
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

    if command.startswith('add:'):
        charname = str(message.author)
        path = '/Users/kawaiikiana/Documents/Luna/Servers/%s/read.txt' % (message.server.id)
        temp = open(path, 'r')
        lines = temp.readlines()
        check = lines[0]
        number = lines[4] 
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
            said = str(command)
            said = said.replace('add:','')
            item, price = said.split(':')
            price = price.replace(',','')
            price = int(price)
            price = '{:,}'.format(price)
            newline = '[' + number + ']' + ':' + '[' + charname + ']' + ':' + '[' + item + ']' + ':' + price + ' Kamas\n'
            path2 = '/Users/kawaiikiana/Documents/Luna/Servers/%s/database.txt' % (message.server.id)
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

    if command.startswith('list'):
        path = '/Users/kawaiikiana/Documents/Luna/Servers/%s/read.txt' % (message.server.id)
        temp = open(path, 'r')
        lines = temp.readlines()
        check = lines[0]

        path2 = '/Users/kawaiikiana/Documents/Luna/Servers/%s/database.txt' % (message.server.id)
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

    if command.startswith('remove '):
        name = '{0.author.mention}/'.format(message)
        name = name.replace('!', '')
        name = name.replace('<', '')
        name = name.replace('>', '')

        said = str(command)
        said = said.replace('remove ','')
        charname = str(message.author)

        path = '/Users/kawaiikiana/Documents/Luna/hotdog/mods.txt'
        temp = open(path, 'r')
        lines = temp.readlines()
        check = lines[0]

        path2 = '/Users/kawaiikiana/Documents/Luna/Servers/%s/database.txt' % (message.server.id)
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

        role = discord.utils.get(message.server.roles,name='Luna Mod')

        for r in message.author.roles:
            if str(r.name) in str(role):
                allowed = 1
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

    if command.startswith('help'):
        response = '```diff\n'
        response += '=======[ Auction Market Commands ]=======\n\n'
        response += '+list\n'
        response += '   - shows all items listed on the market.\n\n'
        response += '+view\n'
        response += '   - shows only your listings on the market.\n\n'      
        response += '+add:[itemName]:[Price]\n'
        response += '   - adds an item to the market, remove the brackets [ ]\n\n'
        response += '+remove [id]\n'
        response += '   - removes an item from the market.\n'
        response += '   - note: only works on items you listed\n\n'
        response += '+search [term]\n'
        response += '   - lists any items on market that include the term\n\n'
        response += '+bid\n'
        response += '   - bids on the item currently up for auction.\n'
        response += '   - only works if there is an auction currently in progress.\n'
        response += '```'
        response += '```diff\n'
        response += '=======[ Mod Commands ]=======\n\n'
        response += '+setprefix [prefix]\n'
        response += '   - changes Luna\'s prefix, remove the brackets [ ]'
        response += '+astart\n'
        response += '   - begins an auction\n'
        response += '```'
        response += '```diff\n'
        response += '=======[ Misc. Commands ]=======\n\n'
        response += '+hotdog\n'
        response += '+ping\n'
        response += '+am\n'
        response += '+hello\n'
        response += '```\n'
        response += '```\n+info for more information.```'
        await client.send_message(message.channel, str(response))

    if command.startswith('lunafixfiles'):
        print("Files created or fixed for the server [%s]!" % (message.server.name))
        folder = '/Users/kawaiikiana/Documents/Luna/Servers/%s' % (message.server.id)
        file1 = '/Users/kawaiikiana/Documents/Luna/Servers/%s/database.txt' % (message.server.id)
        file2 = '/Users/kawaiikiana/Documents/Luna/Servers/%s/read.txt' % (message.server.id)
        file3 = '/Users/kawaiikiana/Documents/Luna/Servers/%s/timer.txt' % (message.server.id)
        file4 = '/Users/kawaiikiana/Documents/Luna/Servers/%s/info.txt' % (message.server.id)

        if not os.path.exists(folder):
            os.makedirs(folder)
            if os.path.exists(folder):
                hotdog = open(file1, 'w+')
                hotdog.close()
                chilidog = open(file2, 'w+')
                chilidog.write('auction:yes\nmessagedel:no\nmessageedit:no\ntimer:0\nnumber:1')
                chilidog.close()
                corndog = open(file3, 'w+')
                corndog.close()
                pizza = open(file4, 'w+')
                pizza.close()
                await client.send_message(message.channel, 'Server files have been created. :ok_hand:')
        if not os.path.exists(file1):
            hotdog = open(file1, 'w+')
            hotdog.close()
            await client.send_message(message.channel, ':ok: Database file has been fixed.')
        if not os.path.exists(file2):
            chilidog = open(file2, 'w+')
            chilidog.close()
            await client.send_message(message.channel, ':ok: Misc. file has been fixed.')
        if not os.path.exists(file3):
            corndog = open(file3, 'w+')
            corndog.close()
            await client.send_message(message.channel, ':ok: Auction timer file has been fixed.')
        if not os.path.exists(file4):
            pizza = open(file4, 'w+')
            pizza.close()
            await client.send_message(message.channel, ':ok: Auction information file has been fixed.')

    if command.startswith('search '):
        term = command.replace('search ','')
        term = str(term)
        temp = open('/Users/kawaiikiana/Documents/Luna/Servers/%s/database.txt' % (message.server.id), 'r')
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

    if command.startswith('view'):
        user = str(message.author)
        view = open('/Users/kawaiikiana/Documents/Luna/Servers/%s/database.txt' % (message.server.id), 'r')
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

    if command.startswith('astart'):
        name = '{0.author.mention}/'.format(message)
        name = name.replace('!', '')
        name = name.replace('<', '')
        name = name.replace('>', '')

        path = '/Users/kawaiikiana/Documents/Luna/hotdog/mods.txt'
        temp = open(path, 'r')
        lines = temp.readlines()
        check = lines[0]

        path2 = '/Users/kawaiikiana/Documents/Luna/Servers/%s/database.txt' % (message.server.id)
        hotdog = open(path2, 'r')
        lines3 = hotdog.read()
        hotdog.close()
        hotdog2 = open(path2, 'r')
        allowed = 0

        role = discord.utils.get(message.server.roles,name='Luna Mod')
        for r in message.author.roles:
            if str(r.name) in str(role):
                allowed = 1

        if name in check:
            allowed = 1

        if allowed == 1:
            if lines3 == '':
                response = 'There are no items up for auction.'
                await client.send_message(message.channel, str(response))

            if not lines3 == '':
                lines2 = hotdog2.readlines()
                auction = lines2[0]
                number, user, item, price = auction.split(':')
                price = price.replace('\n','')
                path3 = '/Users/kawaiikiana/Documents/Luna/Servers/%s/info.txt' % (message.server.id)
                cheese = open(path3, 'w')
                newlines = auction
                newlines += 'hbid: %s\n' % (price)
                newlines += 'name: none\n'
                cheese.write(newlines)
                cheese.close()

                path4 = '/Users/kawaiikiana/Documents/Luna/Servers/%s/timer.txt' % (message.server.id)
                pickle = open(path4, 'w')
                newlines = 'timer: 15'
                pickle.write(newlines)
                pickle.close()

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
                await gofast(server=str(message.server.id), channel=str(message.channel.id))

    if command.startswith('bid'):
        path = '/Users/kawaiikiana/Documents/Luna/Servers/%s/timer.txt' % (message.server.id)
        cake = open(path, 'r')
        check = cake.read()
        check = check.replace('timer: ','')
        check = int(check)
        if check > 0:

            name = str(message.author)

            path = '/Users/kawaiikiana/Documents/Luna/Servers/%s/info.txt' % (message.server.id)
            temp = open(path, 'r')
            lines = temp.readlines()

            nameline = lines[0]
            trash, oname, garbage, junk = nameline.split(':')
            oname = oname.replace('[','')
            oname = oname.replace(']','')

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
                response = "You may not bid if you're the previous bidder <:gobball:373905696502185984>"
                await client.send_message(message.channel, str(response))

            if name == oname:
                allowed = 0
                response = "You may not bid if you're the owner <:gobball:373905696502185984>"
                await client.send_message(message.channel, str(response))

            if allowed == 1:
                if message.content == str(prefix) + 'bid':
                    bid = lowbid
                if message.content.startswith(str(prefix) + 'bid '):
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

                    xelor = '/Users/kawaiikiana/Documents/Luna/Servers/%s/timer.txt' % (message.server.id)
                    relish = open(xelor, 'w')
                    newlines = 'timer: 15'
                    relish.write(newlines)

                    response = '%s has bid %s kamas!' % (name, bid)
                    await client.send_message(message.channel, str(response))

        if check == 0:
            path = '/Users/kawaiikiana/Documents/Luna/Servers/%s/info.txt' % (message.server.id)
            temp = open(path, 'r')
            lines = temp.readlines()
            line = lines[0]
            trash, name, item, kama = line.split(':')
            item = item.replace('[','')
            item = item.replace(']','')
            item = str(item)
            response = 'Oops! Too late-- bidding for %s has ended.' % (item)
            await client.send_message(message.channel, str(response))

client.run("bot token")
