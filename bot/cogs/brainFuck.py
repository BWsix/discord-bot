import requests
from discord.ext import commands

BRAINFUCK_API_BASE_URL = "https://brainfuck-api.vercel.app/api/"

class BrainFuck(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command(name='bf')
  async def bf(self, ctx: commands.Context, *code: str):
    """Executes BrainFuck code."""

    code = "".join(code)

    res = requests.post(
      BRAINFUCK_API_BASE_URL + "execute",
      {"code": code}
    )
    res = res.json()
    
    await ctx.send(res.get("error") or res["output"]["str"])

  @commands.command(name='ttbf')
  async def ttbf(self, ctx: commands.Context, *text: str):
    """Converts text to BrainFuck code."""
    
    text = " ".join(text)

    res = requests.post(
      BRAINFUCK_API_BASE_URL + "convert",
      {"text": text}
    )
    res = res.json()

    await ctx.send(res.get("error") or res["code"])
