import requests
import io
import discord
from discord.ext import commands

BRAINFUCK_API_BASE_URL = "https://qrcode-api-vflc.vercel.app/api/image"

class QRCode(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command(name='qr')
  async def qr(self, ctx: commands.Context, url: str):
    res = requests.post(
      BRAINFUCK_API_BASE_URL,
      {"url": url}
    )

    try:
      stream = io.BytesIO(res.content)
      await ctx.send(file=discord.File(stream, filename="url.png"))
    except Exception as error:
      await ctx.send(error)
