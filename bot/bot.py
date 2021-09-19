from bot.cogs.stuff import Stuff
from bot.cogs.brainFuck import BrainFuck
from bot.cogs.qrCode import QRCode
from bot.cogs.image2Ascii import Image2Ascii
from bot.cogs.weeb import Weeb

import discord
from discord.ext import commands

class BobTheBot(commands.Bot):
  async def on_ready(self):
    print(f"{self.user} is now ready!")

def run(token: str):
  bot = BobTheBot(command_prefix="!", intents=discord.Intents.all())
  cogs = [
    Stuff,
    BrainFuck,
    QRCode,
    Image2Ascii,
    Weeb,
  ]

  for cog in cogs:
    bot.add_cog(cog(bot))

  bot.run(token)
