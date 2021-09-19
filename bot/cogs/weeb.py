from discord.ext import commands
from discord import Message, Embed, Member
from discord.channel import TextChannel
from discord.message import MessageReference
from random import choice, randint

class Weeb(commands.Cog): 
  def __init__(self, bot: commands.Bot):
    self.bot = bot

    bot.add_listener(self.weeb, "on_message")

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

  async def weeb(self, message: Message):
    channel: TextChannel = message.channel

    if message.author == self.bot.user: return
    if channel.name.find("weeb") == -1: return 
    if not message.content: return

    lines = "" 

    for line in message.content.split("\n"):
      if not line:
        lines += '\n'
        continue

      lines += self.transform(line) + '\n'

    if not lines: return 

    try:
      author: Member = message.author

      embed= Embed(description=lines, colour=author.color)
      embed.set_author(
        name=f"{author.display_name} #{author.top_role}",
        icon_url=author.avatar_url
      )

      ref: MessageReference = message.reference
      if ref and (ref.guild_id == channel.guild.id) and (ref.channel_id == channel.id):
        await channel.send(embed=embed, reference=ref)
      else:
        await channel.send(embed=embed)

      await message.delete()
    except Exception:
      pass
