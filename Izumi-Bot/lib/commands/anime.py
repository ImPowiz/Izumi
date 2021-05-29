
from random import randrange
from jikanpy import AioJikan
from jikanpy import Jikan
import asyncio
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
from lib.util.animeinfo import allgenres
from lib.bot.__init__ import botname, botnick

class Anime(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.cancelled = False


    @command(aliases = ['animesearch', 'asearch'])
    async def anime(self, ctx, *, search):
      await ctx.channel.purge(limit=1)
      async with AioJikan() as aio_jikan:
        info = await aio_jikan.search(search_type='anime', query=search)

      anime = info['results'][0]
      embed = discord.Embed(title = anime['title'], color = colord['Pink'])
      embed.set_image(url=anime['image_url'])
      embed.add_field(name = 'Descrption', value = anime['synopsis'], inline = True)
      embed.add_field(name = 'Score:', value = anime['score'])
      embed.add_field(name = 'Type:', value = anime['type'], inline = True)
      embed.add_field(name = 'Episodes:', value = anime['episodes'])
      embed.add_field(name = 'Rating:', value = anime['rated'], inline = True)
      embed.add_field(name = 'Members:', value = str(anime['members']))
      embed.add_field(name = 'Read More:', value = anime['url'], inline = True)
      embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Requested anime by {ctx.author.name}.')
 
      await ctx.send(embed = embed)

    @command(aliases = ['charsearch', 'char'])
    async def character(self, ctx, *, search):
      await ctx.channel.purge(limit=1)
      async with AioJikan() as aio_jikan:
        info = await aio_jikan.search(search_type='character', query=search)

      char = info['results'][0]
      print(char)
      print(char['url'])
      embed = discord.Embed(title = char['name'], color = colord['Pink'])
      embed.set_image(url=char['image_url'])
      embed.add_field(name = 'From:', value = char['anime'][0]['name'], inline = True)
      embed.add_field(name = 'Read More:', value = char['url'], inline = False)
      embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Requested character by {ctx.author.name}.')
 
      await ctx.send(embed = embed)

    @command(aliases = ['genre'])
    async def findanime(self, ctx, *, search):
      await ctx.channel.purge(limit=1)
      
      if search in allgenres:
        jikan = Jikan()

        genre = jikan.genre(type = "anime", genre_id =allgenres[search])

        char = genre['anime'][randrange(int(len(genre['anime'])))]

        async with AioJikan() as aio_jikan:
          info = await aio_jikan.search(search_type='anime', query=char['title'])

          anime = info['results'][0]
          embed = discord.Embed(title = anime['title'], color = colord['Pink'])
          embed.set_image(url=anime['image_url'])
          embed.add_field(name = 'Descrption', value = anime['synopsis'], inline = True)
          embed.add_field(name = 'Score:', value = anime['score'])
          embed.add_field(name = 'Type:', value = anime['type'], inline = True)
          embed.add_field(name = 'Episodes:', value = anime['episodes'])
          embed.add_field(name = 'Rating:', value = anime['rated'], inline = True)
          embed.add_field(name = 'Members:', value = str(anime['members']))
          embed.add_field(name = 'Read More:', value = anime['url'], inline = True)
          embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Random Result for {search} genre for {ctx.author.name}.')
 
      await ctx.send(embed = embed)

    @command()
    async def mal(self, ctx, *, search):
      await ctx.channel.purge(limit=1)
      jikan = Jikan()
      user = jikan.user(username=search)
      
      favanime =[]
      favchar = []

      for item in user['favorites']['anime']:
        favanime.append(item['name'])
  
      for item in user['favorites']['characters']:
        favchar.append(item['name'])

      favanime = "\n".join(favanime)
      favchar = "\n".join(favchar)
  

      embed = discord.Embed(title = f"{user['username']}'s Profile:", color = colord['Pink'])
      embed.set_image(url=user['image_url'])
      embed.add_field(name = 'Days Watched', value = user['anime_stats']['days_watched'], inline = True)
      embed.add_field(name = 'Completed Anime:', value = user['anime_stats']['completed'])
      embed.add_field(name = 'Planning to Watch:', value = user['anime_stats']['plan_to_watch'], inline = True)
      embed.add_field(name = 'Favorite Anime:', value = favanime)
      embed.add_field(name = 'Favorite Characters:', value = favchar, inline = True)
      embed.add_field(name = 'Read More:', value = user['url'], inline = True)
      embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Requested MAL User for {ctx.author.name}.')
 
      await ctx.send(embed = embed)



    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("anime")

def setup(bot):
    bot.add_cog(Anime(bot))