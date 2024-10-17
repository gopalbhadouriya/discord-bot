import discord
from discord.ext import commands


# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'Enter you discord-bot tokin'

# Intents are required for bots interacting with guild members, messages, etc.
intents = discord.Intents.default()
intents.message_content = True


# Set command prefix for the bot (e.g., !help)
bot = commands.Bot(command_prefix='', intents=intents)

# Event for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('Bot is ready!')
    await bot.tree.sync()

# Command for a simple response
@bot.command()
async def hello(ctx):
    await ctx.send(f'hello😊,and how are you😊, {ctx.author.mention}!')

@bot.command()
async def wtf(ctx):
    await ctx.send(f'fucky😡, {ctx.author.mention}!')
    
@bot.command()
async def bye(ctx):
    await ctx.send(f'Good day😃, {ctx.author.mention}!')

@bot.command()
async def f(ctx):
    await ctx.send(f'get lost away😡, {ctx.author.mention}!')

@bot.command()
async def hii(ctx):
    await ctx.send(f'hii😊,how are you,please don\'t take space in you words to chat me😁, {ctx.author.mention}!')

@bot.command()
async def first_bot(ctx):
    await ctx.send(f'hii,how can i help you 😊, {ctx.author.mention}!')
    
@bot.command()
async def sorry(ctx):
    await ctx.send(f'ok,Don\'t do this again🤨 , {ctx.author.mention}!')

@bot.command()
async def howareyou(ctx):
    await ctx.send(f'i am fine and how are you 😊 , {ctx.author.mention}!')

@bot.command()
async def iamfine(ctx):
    await ctx.send(f'i wish you always fine 😊 , {ctx.author.mention}!')
    
@bot.command()
async def howareu(ctx):
    await ctx.send(f'i am fine and how are you 😊 , {ctx.author.mention}!')

@bot.command()
async def why(ctx):
    await ctx.send(f'becouse i can\'t understant space🤗 ,i can only type space 😄, {ctx.author.mention}!')

@bot.command()
async def ok(ctx):
    await ctx.send(f'Wow you are so wise 🤔,you understanded me,thank you😊,let\'s chat with me🙂, {ctx.author.mention}!')


# Run the bot
bot.run(TOKEN)
