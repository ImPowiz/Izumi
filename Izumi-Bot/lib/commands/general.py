import os
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext import commands
from random import choice
import discord
from discord import Member

from datetime import datetime, timezone
from lib.util.info import InfoTemplate
from lib.util.colors import colord
from lib.util.cmd import cmdinfo
from lib.util.cmd import acatagory
from lib.util.cmd import Updates
from lib.util.cmd import log
from lib.util.funtions import RandomChoice2
from lib.util.funtions import update_tree
from lib.util.actions import adjectives
from lib.util.actions import eactions
from lib.util.actions import actions
from lib.util.actions import Sactionsdef
from lib.util.actions import Sactions

class General(Cog):
    def __init__(self,bot):
        self.bot = bot


    @command(aliases=["cmd", "commands"])
    async def helpme(self, ctx, *,catagory='N/A'):
      prefix = '.'
      if 'N/A' in catagory:

        embed = discord.Embed(title="**Command Catagories: **",
	      color=colord['Blue'])

        embed.add_field(name=f'Prefix: {prefix}',
	      value='•-•-•-•-•-•-•-•-•',
	      inline=True)

        embed.add_field(name='**General Commands: **',
	      value='cmd general',
	      inline=False)

        embed.add_field(name='**Image Commands: **', value='cmd image', inline=False)

        embed.add_field(name='**Action Commands: **',
	      value='cmd actions',
	      inline=False)

        embed.add_field(name='**Fun Commands: **', value='cmd fun', inline=False)

        embed.add_field(name='**Giveaway Commands: **', value='cmd giveaway', inline=False)

        embed.add_field(name='**Anime Commands: **', value='cmd anime', inline=False)
      else:
        if catagory in cmdinfo:
          embed = discord.Embed(title=f'**{acatagory[catagory]}:**',
          color=colord['Blue'])
          embed.add_field(name='•-•-•-•-•-•-•-•-•', value=cmdinfo[str(catagory)], inline=True)
        else:
          embed = discord.Embed(title=f'**Catagory not found.**',
          color=colord['Blue'])
          embed.add_field(name='•-•-•-•-•-•-•-•-•', value="Maybe  try using cmd?", inline=True)
  

      embed.set_footer(icon_url=ctx.author.avatar_url, text=Updates)
      await ctx.send(embed=embed)


#shows info about user
    @command(aliases = ['whois', 'user'])
    async def info(self, ctx, *, member: discord.Member):
      x = datetime.now()

      pdthr = int(x.strftime("%H")) + 5

      if pdthr > 24:
        hr = str(pdthr - 7)
        ampm = 'pm'
      else:
        if pdthr > 12:
          hr = str(pdthr - 12)
          ampm = 'pm'
        else:
          if pdthr - 5 < 6:
           hr = str(pdthr)
           ampm = 'pm'
          else:
            hr = str(pdthr)
            ampm = 'am'

      minute = int(x.strftime("%M"))

      message = f'Today at: {hr}:{minute}{ampm}'

      seperator = '•-•-•-•-•-•-•-•-•'

      embed = discord.Embed(title=f"{member.name}'s Profile",
	                      color=colord['Blue'])
      created_at = member.created_at.strftime("%b %d, %Y")
      embed.add_field(name=f'{seperator}', value='\n**:**', inline=True)
      embed.add_field(name='ID', value=member.id, inline=False)
      embed.add_field(name='Joined Discord On:', value=created_at, inline=False)
      embed.add_field(name=":", value=f'{seperator}', inline=False)
      embed.set_thumbnail(url=member.avatar_url)
      embed.set_footer(icon_url=ctx.author.avatar_url,text=f'Requested by {ctx.author.name} | {message}')
      await ctx.channel.purge(limit=1)
      await ctx.send(embed=embed)
      
    @command(aliases = ['welcome'])
    async def wc(self, ctx, *, member: discord.Member):
      x = datetime.now()

      pdthr = int(x.strftime("%I")) + 5

      if pdthr > 12:
        hr = str(pdthr - 12)
        ampm = 'pm'
      else:
        hr = str(pdthr)
        ampm = 'am'

      minute = int(x.strftime("%M"))

      message = f'Today at: {hr}:{minute}{ampm}'

      embed = discord.Embed(title=f'Hi {member.name}!',descrpition=member.mention, color=colord['Blue'])

      seperator = '•-•-•-•-•-•-•-•-•'

      embed.add_field(name=f'{seperator}', value=InfoTemplate, inline=True)
      embed.add_field(name="**:**", value=f'{seperator}', inline=False)
      embed.set_thumbnail(url=member.avatar_url)
      embed.set_footer(icon_url=member.avatar_url,  text=f'Welcome to the server! • {message}')
      await ctx.send(embed=embed)
      
#Shows actionlist
    @command(aliases=["termlist", "al", "actionlist", 'actions', 'terms'])
    async def tl(self, ctx):
      allacts = actions + eactions + adjectives
      embed = discord.Embed(title='Action List:', color=colord['Teal'])
      embed.add_field(name='Avaliable Terms', value=allacts)

      await ctx.send(embed=embed)
    

    @command(name="cmd giveaway", aliases=["ghelp", "givhelp", "givehelp"])
    async def help_user(self, ctx):
        embed = discord.Embed(title="Giveaway setup Help",
                      description="Setup Your giveaway in some simple commands",
                      color=ctx.author.color)
        embed.add_field(name="Create Giveaway", value="Create a giveaway by using the .giveaway command. You can also .giftcr.The bot will ask some simple questions to host your giveaway.")
        embed.add_field(name="Reroll Giveaway", value="Reroll a giveaway again by using the !gifreroll command. Additionally you can also use commands like .gftroll or .giftrrl. The bot will ask some simple questions to host your giveaway.")
        embed.add_field(name="Cancel Giveaway", value="Delete a giveaway by using the .giftdel command. Additionally you can also use commands like .gftdel or .gifdel. The bot will ask some simple questions to host your giveaway.")
        await ctx.send(embed=embed)
    
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.command_ready.ready_up("general")
    

def setup(bot):
    bot.add_cog(General(bot))


