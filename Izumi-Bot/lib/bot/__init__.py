from discord.utils import find
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import Context
from discord.ext.commands import CommandNotFound, BadArgument
from discord.ext.commands import MissingRequiredArgument, MissingRole, MissingPermissions
from discord.errors import Forbidden
from discord import Embed, File, Intents
from glob import glob
from datetime import datetime, timezone
from asyncio import sleep
import discord
from lib.util.info import InfoTemplate
from lib.util.colors import colord
from lib.util.statuses import status
from lib.util.funtions import boldText
import random
from asyncio import sleep
from prsaw import RandomStuff
from replit import db


intents = discord.Intents.all()
tbot = commands.Bot(command_prefix = '.', intents=intents)
prefix = '.'
rs = RandomStuff(async_mode = True)

botname = str(tbot.user)
botnick = str(tbot.user)

@tbot.event
async def on_member_join(member):
  print('It worked.')
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
  await tbot.get_channel(755517533343318039).send(embed=embed)



PREFIX = "."
OWNER_IDS = [424652015227109376]
COMMANDS = [path.split("/")[-1][:-3] for path in glob("./lib/commands/*.py")]
IGNORE_EXCEPTIONS = [CommandNotFound, BadArgument]
class Ready(object):
    def __init__(self):
        for command in COMMANDS:
            setattr(self, command, False)
    def ready_up(self, command):
        setattr(self, command, True)
        print(f"{command} commands are ready.")

    def all_ready(self):
        return all([getattr(self, command) for command in COMMANDS])

class Bot(BotBase):
    prefix = '.'
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.command_ready = Ready()
        self.guild = None


        super().__init__(command_prefix=PREFIX, OWNER_ID=OWNER_IDS)

    def setup(self):
        print("setup Run")
        for command in COMMANDS:
            self.load_extension(f"lib.commands.{command}")
            print(f"{command} cog Loaded")

    def run(self, token):
        print("running setup")
        self.setup()
        self.TOKEN = token
        print("Running Bot...")
        super().run(self.TOKEN, reconnect=True)

    async def process_commands(self,message):
        ctx = await self.get_context(message, cls=Context)
        if ctx.command is not None and ctx.guild is not None:
          await self.invoke(ctx)
    
    async def on_connect(self):
        print("Konichiwa Senpai!")

    async def on_disconnect(self):
        print("Ara ara, sayanora!")

    async def on_error(self, err, ctx, *args, **kwargs):
        if err == 'on_command_error':
            await ctx.send("An error Occurrred")
        raise 

    async def on_command_error(self, ctx, exc):
      if isinstance(exc, commands.CommandOnCooldown):
        secs = '{:.2f}'.format(exc.retry_after)
        mins = round(int(float(secs)) // 60)
        if round(float(secs)) < 60:
          msg = f'**Still on cooldown**, please try again in {secs} seconds.'
        else:
          msg = f'**Still on cooldown**, please try again in  {mins} minutes.'

        await ctx.send(msg)
        if any([isinstance(exc, err) for err in IGNORE_EXCEPTIONS]):
            pass

        elif isinstance(exc, MissingRequiredArgument):
            await ctx.send("One or More argument required!")

        elif isinstance(exc, MissingPermissions):
            await ctx.send("You are not allowed to create Giveaways.")

        elif isinstance(exc, MissingRole):
            await ctx.send("You do not have the necessary role to create Giveaways.")
        
        elif hasattr(exc, "original"):
            if isinstance(exc.original, Forbidden):
                await ctx.send("I don't have permission to do that!!")
            else:
                raise exc.original
        else:
            raise exc



    async def on_ready(self):
        async def status_task():
          while True:
            await self.change_presence(status=discord.Status.idle,          activity=discord.Game(random.choice(status)))
            await sleep(4)
            await self.change_presence(status=discord.Status.idle,          activity=discord.Game(random.choice(status)))
            await sleep(4)
        if not self.ready:

            while not self.command_ready.all_ready():
                print("waiting......")
                await sleep(0.5)
            self.ready = True
            print("Bot ready")
            self.loop.create_task(status_task())


          

    async def on_guild_join(self, guild):
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
      general = str.find(lambda x: x.name == 'general', guild.text_channels)
  
      if general and general.permissions_for(guild.me).send_messages:
        embed = discord.Embed(title=f"{bot.name} is now in your server!", description="Hello! Thanks for inviting me, you're such a nice server!", colour=0x00FFFF)
        embed.set_author(name=guild.name)
        embed.set_thumbnail(url=bot.avatar_url)
        embed.set_footer(message)
        await general.send(embed=embed)

      async def on_member_join(self, member):
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
        await bot.get_channel(755517533343318039).send(embed=embed)


    async def on_message(self, message):
        if not message.author.bot:
          if int(message.author.id) in db['muted']:
            await message.channel.purge(limit=1)

          if self.user.mention == message.content:
            await message.channel.send('**Use .cmd for a list of commands!')
          
          if '>' in message.content[0]:
            talkai = message.content[1:]
            response = await rs.get_ai_response(talkai)
            await message.channel.send(boldText(response))
            return
          
          
            
        await self.process_commands(message)


bot = Bot()