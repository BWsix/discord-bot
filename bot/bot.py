from os import environ
import discord
from discord.ext import commands

from bot.cogs.stuff import Stuff
from bot.cogs.brainFuck import BrainFuck
from bot.cogs.qrCode import QRCode

class BobTheBot(commands.Bot):
  async def on_ready(self):
    print(f"{self.user} is now ready!")

def run():
  bot = BobTheBot(command_prefix="!", intents=discord.Intents.all())
  bot.add_cog(Stuff(bot))
  bot.add_cog(BrainFuck(bot))
  bot.add_cog(QRCode(bot))

  bot.run(environ.get("BOT_TOKEN"))
