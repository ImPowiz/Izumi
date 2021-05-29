
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
from discord import Member
from replit import db
import nekos
import random
from discord import Embed,File
from lib.util.colors import colord

from lib.util.funtions import action
from lib.util.funtions import RandomGif
from lib.bot.__init__ import botname, botnick


from lib.util.actions import adjectives, eactions, actions,Sactionsdef, Sactions


class Action(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.cancelled = False

#baka
    @command(name="baka", aliases = [])
    async def baka(self, ctx, *, member: discord.Member = None):
	    if member == None:
		    response = 'BAKA!'
	    else:
		    response = f"You are a baka, {member.name}!"

	    gifsearch = (action(("baka")))
	    giflink = RandomGif(gifsearch)
	    gif = giflink.replace("'", ' ').replace(",", ' ')

	    embed = discord.Embed(title=response, color=colord['Teal'])
	    embed.set_image(url=gif)

	    await ctx.send(embed=embed)
	    print(gif)


    #action
    @command(name='call', aliases=actions)
    async def call_action(self, ctx, *, member: discord.Member = None):
      if member == None:
        response = ctx.author.name + " is " + ctx.invoked_with + "ing" + "!"
      else:
        if str(ctx.invoked_with) in Sactions:
         response = f"{ctx.author.name} is {Sactionsdef[str(ctx.invoked_with)]} {member.name}!"
        else:
          response = ctx.author.name + " is " + ctx.invoked_with + "ing  " + member.name + "!"


      gifsearch = (action(("anime" + ctx.invoked_with)))
      giflink = RandomGif(gifsearch)
      gif = giflink.replace("'", ' ').replace(",", ' ')

      embed = discord.Embed(title=response, color=colord['Teal'])
      embed.set_image(url=gif)
      await ctx.channel.purge(limit=1)
      await ctx.send(embed=embed)
      print(gif)
      if botname in response or botnick in response:
        if str(ctx.invoked_with) in Sactions:
          response = f"I'm {Sactionsdef[str(ctx.invoked_with)]} {ctx.author.name} back!"
        else:
          response ="I'm " + ctx.invoked_with + "ing  " + ctx.author.name + " back!"


        gifsearch = (action(("anime" + ctx.invoked_with)))
        giflink = RandomGif(gifsearch)
        gif = giflink.replace("'", ' ').replace(",", ' ')

        embed = discord.Embed(title=response, color=colord['Teal'])
        embed.set_image(url=gif)
        await ctx.send(embed=embed)



    #action
    @command(aliases=eactions)
    async def wave(self, ctx, *, member: discord.Member = None):
      await ctx.channel.purge(limit=1)
      if member == None:
	      response = ctx.author.name + " is " + ctx.invoked_with[:-1] + "ing" + "!"
      else:
        if str(ctx.invoked_with) in Sactions:
          response = f"{ctx.author.name} is {Sactionsdef[str(ctx.invoked_with)]} {member.name}!"
        else:
          response = ctx.author.name + " is " + ctx.invoked_with[:
		         -1] + "ing  " + member.name + "!"

    
      gifsearch = (action(("anime" + ctx.invoked_with)))
      giflink = RandomGif(gifsearch)
      gif = giflink.replace("'", ' ').replace(",", ' ')

      embed = discord.Embed(title=response, color=colord['Teal'])
      embed.set_image(url=gif)
      await ctx.send(embed=embed)
      print(gif)
      if 'Powiz Bot' in response:
        if str(ctx.invoked_with) in Sactions:
          response = f"I'm {Sactionsdef[str(ctx.invoked_with)]} {ctx.author.name} back!"
        else:
          response ="I'm " + ctx.invoked_with[:
    		 -1] + "ing  " + ctx.author.name + " back!"


        gifsearch = (action(("anime" + ctx.invoked_with)))
        giflink = RandomGif(gifsearch)
        gif = giflink.replace("'", ' ').replace(",", ' ')

        embed = discord.Embed(title=response, color=colord['Teal'])
        embed.set_image(url=gif)
        await ctx.send(embed=embed)



    #feeling
    @command(aliases=adjectives)
    async def sad(self, ctx, *, member: discord.Member = None):
      await ctx.channel.purge(limit=1)
      if member == None:
    	  response = ctx.author.name + " is feeling " + ctx.invoked_with + "!"
      else:
    	  response = ctx.author.name + " is feeling " + ctx.invoked_with + ' because of ' + member.name + "!"

      gifsearch = (action(("anime" + ctx.invoked_with)))
      giflink = RandomGif(gifsearch)
      gif = giflink.replace("'", ' ').replace(",", ' ')

      embed = discord.Embed(title=response, color=colord['Teal'])
      embed.set_image(url=gif)
      await ctx.send(embed=embed)
      print(gif)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("action")

def setup(bot):
    bot.add_cog(Action(bot))