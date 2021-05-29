from discord.ext.commands import Cog
from discord.ext.commands import command, has_permissions, has_role
import discord
from discord import Member
from discord import Embed,File
from typing import Optional
from random import choice
from asyncio import TimeoutError, sleep
from lib.util.convert_time import convert

import discord
from discord.ext import commands
from replit import db
import nekos
import random
from lib.util.colors import colord

from lib.util.nekosearches import possible
from lib.util.nekosearches import nsfw

from lib.util.jokes import jokes
from lib.util.jokes import videos
from lib.util.jokes import puns

from lib.util.yes_or_no import yes_or_no
from lib.util.general_questions import questions
from lib.util.WYR_Questions import wyrq

from lib.util.funtions import action
from lib.util.funtions import RandomGif
from lib.util.funtions import boldText
from lib.util.funtions import RandomChoice
from lib.util.funtions import RandomChoice2
from lib.util.funtions import update_tree




#fun commands

class Fun(Cog):
    def __init__(self,bot):
        self.bot = bot
        

#8ball
    @command(name="_8ball", aliases=["8b"])
    async def _8ball(self, ctx, *, question):

	    response = (f"Question: {question}\nAnswer: {(random.choice(yes_or_no))}")

	    embed = discord.Embed(title="8 ball has decided..",
	                      description=response,
	                      color=colord['Purple'])
	    embed.set_thumbnail(
	    url=
	    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/8-Ball_Pool.svg/1024px-8-Ball_Pool.svg.png')
	    await ctx.send(embed=embed)

#topic
    @command(name="qe", aliases=["question", "topic", "randomtopic"])
    async def _q(self, ctx):

	    response = str(RandomChoice(questions))

	    embed = discord.Embed(title=response, color=colord['Purple'])

	    await ctx.send(embed=embed)

    #say
    @command(name="say", aliases=["s"])
    async def say(self, ctx, *, search):

      response = f"{ctx.author.name} said '{search}'"
      gifsearch = (action((search)))

      giflink = RandomGif(gifsearch)
      gif = giflink.replace("'", ' ').replace(",", ' ')

      embed = discord.Embed(title=response, color=colord['Purple'])
      embed.set_image(url=gif)
      await ctx.send(embed=embed)
      print(gif)

#wyr
    @command(name='wyr', aliases = [])
    async def wyr(self, ctx):

	    response = RandomChoice(wyrq)

	    embed = discord.Embed(title=response, color=colord['Purple'])

	    await ctx.send(embed=embed)

    #pick
    @command(name="choose", aliases = ['pick', 'random'])
    async def choose(self, ctx, *, list):
      starter = random.choice(['Personally, I prefer', "I'd choose", 'The only right choice would be'])
      response = f"{starter} {RandomChoice2(list)}"

      embed = discord.Embed(title=response, color=colord['Purple'])

      await ctx.send(embed=embed)


#funny stuff
    @command(name="video", aliases=['joke', 'pun', 'badpun'])
    async def video(self, ctx):
	    if ctx.invoked_with == 'video':
		    response = f"Here's a random video:\n<{random.choice(videos)}>"
	    else:
		    if ctx.invoked_with == 'pun' or ctx.invoked_with == 'badpun':
			    response = f"Here's a random pun:\n{RandomChoice(puns)}"
		    else:
			    if ctx.invoked_with == 'joke':
				    response = f"Here's a random joke:\n{RandomChoice(jokes)}"

	    embed = discord.Embed(title=response, color=colord['Purple'])

	    await ctx.send(embed=embed)


    @command(name="repeat", aliases = [])
    async def repeat(self, ctx, *, message):
      response = message

      embed = discord.Embed(title=response, color=colord['Orange'])

      await ctx.send(embed=embed)
      return

    #planttree
    @commands.cooldown(1,600,commands.BucketType.guild)
    @command(name="planttree", aliases = [])
    async def planttree(self, ctx):

      if "trees" in db.keys():
        totaltrees = db["trees"]

      newtree = int(random.choice(totaltrees)) + 1
      trees = (newtree)

      if "trees" in db.keys():
        db["trees"] = []

      update_tree(trees)

      response = f'A new tree was planted! There are now {trees} trees!'

      embed = discord.Embed(title=response, color=colord['Green'])

      await ctx.send(embed=embed)
      return
  
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("fun")

def setup(bot):
    bot.add_cog(Fun(bot))