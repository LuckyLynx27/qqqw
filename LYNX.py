import random
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'Connected as: {bot.user.name} \nBot ID#: {bot.user.id}')

@bot.command()
async def sayhi():
    greetings=['Hello','Hey','Hi']
    await bot.say(random.choice(greetings))

@bot.command()
async def copy(ctx):
    pass

@bot.command(name='list')
async def _list(ctx, arg):
    pass

@bot.command()
async def echo(message: str):
    await bot.say(message)


@bot.command(pass_context = True)
async def lol(ctx):
    if ctx.message.author.id == "221448768900431872":
        await bot.say('Confirmed!')

    else:
        await bot.say('Denied.')



bot.run('NDUxMTI3NDMxMzk1Mjc4ODYx.De9RMA.9z7-OY2qqJA8OXpOG01lybk1Js8')