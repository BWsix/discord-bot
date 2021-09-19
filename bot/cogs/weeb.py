from discord.ext import commands
from random import choice, randint

class Weeb(commands.Cog): 
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  def transform(self, content: str) -> str:

    def add_postfix(content: str) -> str:
      ACTIONS = [
        "笑",
        "燦笑",
        "推眼鏡",
        "摸頭",
        "茶",
        "歪頭",
        "汗顏",
        "？",
        "ㄏㄏ",
        "喂！",
        "遠望",
        "探頭",
        "搔頭",
        "嘆",
        "扶額",
        "咳咳",
      ]

      return f"{content} ({choice(ACTIONS)}"

    def add_prefix(content: str) -> str:
      WORDS = [
        "嘛",
        "欸都",
        "唔姆",
        "呀咧呀咧",
      ]

      TRAILERS = [
        "",
        "...",
        "~",
      ]

      return f"{choice(WORDS)}{choice(TRAILERS)} {content}"
      
    def add_w(content: str) -> str:
      return f"{content} {'w'*randint(1, 5)}"

    return choice([
      add_prefix,
      add_postfix,
      add_w,
    ])(content)

  @commands.command(name='weeb')
  async def weeb(self, ctx: commands.Context):
    msg: str = ctx.message.content[6:].rstrip()
    lines = "" 

    for line in msg.split("\n"):
      if not line:
        lines += '\n'
        continue

      lines += self.transform(line) + '\n'

    if lines:
      await ctx.send(lines)
