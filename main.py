from lib.bot import bot
from lib.util.info import InfoTemplate
from lib.util.colors import colord
from lib.util.keep_alive import keep_alive
import os
import discord
import json
from discord.ext import commands
import os
import random
from replit import db
from asyncio import sleep
from prsaw import RandomStuff
import nekos
from discord.utils import get
import datetime

my_secret = os.environ['token']

keep_alive()

bot.run(my_secret)
