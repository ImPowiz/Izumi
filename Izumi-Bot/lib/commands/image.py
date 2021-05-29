
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
import nekos
from lib.util.colors import colord
from lib.util.nekosearches import possible
from lib.util.nekosearches import nsfw
from lib.util.funtions import action
from lib.util.funtions import RandomGif
from lib.util.funtions import boldText
from lib.util.funtions import image

#image commands

class Image(Cog):
    def __init__(self,bot):
        self.bot = bot

#GIF
    @command(aliases=['gif'])
    async def g(self, ctx, *, search=None):
      if search == None:
        search = "gif"

      gifsearch = (action((search)))
      giflink = RandomGif(gifsearch)
      gif = giflink.replace("'", ' ').replace(",", ' ')

      embed = discord.Embed(color=colord['Yellow'])
      embed.set_image(url=gif)
      await ctx.send(embed=embed)
      print(gif)

#Anime GIF
    @command(aliases=['animegif', 'ag'])
    async def a(self, ctx, *, search=None):
	    if search == None:
		    gifsearch = (action("anime"))
	    else:
		    gifsearch = (action(("anime" + search)))

	    giflink = RandomGif(gifsearch)
	    gif = giflink.replace("'", ' ').replace(",", ' ')

	    embed = discord.Embed(color=colord['Yellow'])
	    embed.set_image(url=gif)
	    await ctx.send(embed=embed)
	    print(gif)

    @command(aliases = nsfw)
    async def trap(self, ctx):
      if ctx.invoked_with in nsfw:
        if ctx.channel.is_nsfw():
          await ctx.send(nekos.img(target=ctx.invoked_with))
        else:
          await ctx.send(boldText('Since this command has a chance of showing NSFW images, please only use this command in NSFW channels.'))
          return


#nekosss
    @command(aliases=['catgirl'])
    async def neko(self, ctx, *, search=None):

      if search in nsfw:
        if ctx.channel.is_nsfw():
          await ctx.send(nekos.img(target=search))
        else:
          await ctx.send(boldText('Since this tag has a chance of showing NSFW images, please only use this command in NSFW channels.'))
        return

      if search == None or search not in possible:
	      await ctx.send(nekos.img(target='neko'))
      else:
        await ctx.send(nekos.img(target=search))

#cat
    @command(aliases=['kitty'])
    async def cat(self, ctx):
	    await ctx.send(nekos.cat())

#foxgirl
    @command()
    async def foxgirl(self, ctx):
	    await ctx.send(nekos.img(target='fox_girl'))

#displays image
    @command(aliases=['image'])
    async def img(self, ctx, *, link):
  
      embed = discord.Embed(color=colord['White'])
      embed.set_image(url=link)

      await ctx.channel.purge(limit=1)
      await ctx.send(embed=embed)


    #Shows meme
    @command(aliases=['meme'])
    async def m(self, ctx, *, member: discord.Member = None):
      await ctx.channel.purge(limit=1)

      if member == None:
	      response = f"Here's a meme for you {ctx.author.name}!"
      else:
	      response = ctx.author.name + " sent a meme to " + member.name + "!"

      gifsearch = (action(('meme')))
      giflink = RandomGif(gifsearch)
      gif = giflink.replace("'", ' ').replace(",", ' ')

      embed = discord.Embed(title=response, color=colord['Purple'])
      embed.set_image(url=gif)
      await ctx.send(embed=embed)
      print(gif)

    @command()
    async def waifu(self, ctx, *, waifu):

	    gifsearch = (image(('waifu' + waifu)))
	    giflink = RandomGif(gifsearch)
	    gif = giflink.replace("'", ' ').replace(",", ' ')

	    embed = discord.Embed(title=waifu, color=colord['Teal'])
	    embed.set_image(url=gif)

	    await ctx.send(embed=embed)
	    print(gif)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("image")

def setup(bot):
    bot.add_cog(Image(bot))