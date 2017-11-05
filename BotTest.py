#Tutorial https://www.youtube.com/watch?v=u6tBvQSXJ7I
#Python wrapper https://pypi.python.org/pypi/discord.py/
#Note that in Python 3.4 you use `@asyncio.coroutine` instead of `async def` and `yield from` instead of `await`.
#Python 3.5+ use `async def`
#Another tutorial that MIGHT be useful https://www.youtube.com/watch?v=aFI1SItR8tg

#TODO:
#-Look into pass_context, figure out if that's a way to capture reference to last message

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
    for c in channelList:
        await bot.say(str(c.name) + " in server, " 
                    + str(c.server.name))

@bot.command()
async def getServersRaw():
    await bot.say("I can see the following servers: ")
    await bot.say(list(bot.servers))

@bot.command()
async def getServers():
    await bot.say("I can see the following servers: ")
    serverList = list(bot.servers)
    for s in serverList:
        await bot.say(str(s.name))

@bot.command()
async def tryLogin():
    await bot.login(botToken)

bot.run(botToken)
