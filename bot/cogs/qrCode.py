import requests
import urllib
import discord
from discord.ext import commands

BRAINFUCK_API_BASE_URL = "https://qrcode-api-vflc.vercel.app/api"

class QRCode(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command(name='qr')
  async def qr(self, ctx: commands.Context, url: str):
    res = requests.post(
      BRAINFUCK_API_BASE_URL,
      {"url": url}
    )
    res = res.json()

    if error:=res.get("error"):
      return await ctx.send(error)

    try:
      stream = urllib.request.urlopen(res["data"]).file
      await ctx.send(file=discord.File(stream, filename=res["url"]+".png"))
    except Exception:
      await ctx.send("error")
