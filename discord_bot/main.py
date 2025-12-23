# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import logging

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='doscord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send(f"Wellcome to the server {member.name}")
    
@bot.event
async def on_message(message):"
    

bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)

"https://realpython.com/how-to-make-a-discord-bot-python/"
"https://www.youtube.com/watch?v=YD_N6Ffoojw"
