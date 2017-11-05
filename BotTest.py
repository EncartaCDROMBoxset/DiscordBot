#Tutorial https://www.youtube.com/watch?v=u6tBvQSXJ7I
#Add to server link: https://discordapp.com/oauth2/authorize?client_id=your_client_id_goes_here&scope=bot&permissions=0
#Python wrapper https://pypi.python.org/pypi/discord.py/
#Note that in Python 3.4 you use `@asyncio.coroutine` instead of `async def` and `yield from` instead of `await`.
#Python 3.5+ use `async def`
#Another tutorial that MIGHT be useful https://www.youtube.com/watch?v=aFI1SItR8tg

#TODO:
#-Make getChannels organize by server. Probs use a dictionary here.
#-Make the bot post only to a specific channel.
#--If the context is outside of the specified channel, tag the author.
#-MAYBE refactor all these "gets" to helpers, make the current ones "say" functions
#-Make getRoles build a list and return it in sorted alphabetical

#Dictionary
# ServerName : ([Roles], [Channels])

import discord
from discord.ext.commands import Bot
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

@bot.command()
async def tryLogin():
    await bot.login(botToken)

bot.run(botToken)
