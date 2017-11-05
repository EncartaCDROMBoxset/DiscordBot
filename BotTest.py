#Tutorial https://www.youtube.com/watch?v=u6tBvQSXJ7I
#Add to server link: https://discordapp.com/oauth2/authorize?client_id=your_client_id_goes_here&scope=bot&permissions=0
#Python wrapper https://pypi.python.org/pypi/discord.py/
#Note that in Python 3.4 you use `@asyncio.coroutine` instead of `async def` and `yield from` instead of `await`.
#Python 3.5+ use `async def`
#Another tutorial that MIGHT be useful https://www.youtube.com/watch?v=aFI1SItR8tg
#Awesome writeup on Decorators https://realpython.com/blog/python/primer-on-python-decorators/
#For helper functions, you have to await coroutine calls to make sure a result is returned. See https://docs.python.org/3/library/asyncio-task.html

#TODO:
#-Make getChannels organize by server. Probs use a dictionary here.
#-Make the bot post only to a specific channel.
#--If the context is outside of the specified channel, tag the author.
#-MAYBE refactor all these "gets" to helpers, make the current ones "say" functions
#-Make getRoles build a list and return it in sorted alphabetical
#Make creating roles only allowable by roles that can manage roles
#Creating roles needs exception handling
#Refactor roleNames helper to have a general default parameter
#Might be a good idea to have role stuff as subcommands. See the discord.py docs
#Maybe replace string concatenations with {}.format's

#Dictionary
# ServerName : ([Roles], [Channels])

import discord
#from discord.ext.commands import Bot
from discord.ext import commands

botToken = "token"
Client = discord.Client()
bot_prefix="!"
bot = commands.Bot(command_prefix = bot_prefix)
#Server = "server goes here"
TalkChannel = "Channel goes here"

@bot.event
async def on_ready():
    print("Bot online.")
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print(list(bot.servers))

###### Channels ######

@bot.command()
async def getChannelsRaw():
    await bot.say("I can see the following channels: ")
    await bot.say(list(bot.get_all_channels()))

@bot.command()
async def getChannels():
    await bot.say("I can see the following channels: ")
    channelList = list(bot.get_all_channels())
    channelString = ""
    for c in channelList:
    	channelString += str(c.name) + " in server, " + str(c.server.name) + "\n"
    await bot.say(channelString)

###### Roles ######

@bot.command(pass_context = True)
async def createRole(ctx):
	currentRoles = await getRoleNames(ctx)
	print(type(currentRoles))
	rolesToAdd = str(ctx.message.content).split(" ")
	rolesToAdd.remove("!createRole")
	await bot.say("You want me to add the following roles: \n" + " | ".join(rolesToAdd))
	for role in rolesToAdd:
		if role in currentRoles:
			await bot.say(role + " already exists.")
		else:
			await bot.say(role + ", I can create that role.")

@bot.command()
async def getRolesAllServers():
	await bot.say("I can see the following roles: ")
	responseString = ""
	serverList = list(bot.servers)
	for s in serverList:
		responseString += str(s.name) + "\n"
		for role in s.roles:
			if role.is_everyone is not True:
				responseString += "- " + str(role.name) + "\n"
		responseString += "\n"
	await bot.say(responseString)

@bot.command(pass_context = True)
async def getRolesThisServer(ctx):
	await bot.say("I can see the following roles: ")
	responseString = ""
	for role in ctx.message.server.roles:
		if role.is_everyone is not True:
			responseString += "- " + str(role.name) + "\n"
	await bot.say(responseString)

###### Servers ######

@bot.command()
async def getServersRaw():
    await bot.say("I can see the following servers: ")
    await bot.say(list(bot.servers))

@bot.command()
async def getServers():
    await bot.say("I can see the following servers: ")
    serverList = list(bot.servers)
    serverString = ""
    for s in serverList:
        serverString += "- " + str(s.name) + "\n"
    await bot.say(serverString)

###### Helpers ######

#Returns role names of the server from which context originated
async def getRoleNames(ctx):
	roles = ctx.message.server.roles
	roleNames = []
	for role in roles:
		roleNames.append(role.name)
	return roleNames

###### Dev ######

@bot.command()
async def test():
    await bot.say("Hello World!")

@bot.command(pass_context = True)
async def checkContext(ctx):
    await bot.say(str(ctx.message.author) + " messaged me from the channel, " 
                + str(ctx.message.channel) + ", in the server, " 
                + str(ctx.message.server))
    await bot.say("They said: \n" + str(ctx.message.content))

@bot.command()
async def checkStatus():
    await bot.say("is_logged_in: " + str(bot.is_logged_in))
    await bot.say("is_closed: " + str(bot.is_closed))

@bot.command()
async def tryLogin():
    await bot.login(botToken)

bot.run(botToken)
