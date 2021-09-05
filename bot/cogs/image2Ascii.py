from discord.ext import commands
import discord

import numpy as np
import cv2 as cv

WIDTH = 40

class Image2Ascii(commands.Cog): 
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    
  @commands.command(name='itac')
  async def itac(self, ctx: commands.Context):
    attachment: discord.Attachment
    for attachment in ctx.message.attachments:
      if not attachment.content_type.startswith("image"):
        return

      img_array = np.array(bytearray(await attachment.read()), dtype=np.uint8)
      img = cv.imdecode(img_array, flags=cv.IMREAD_GRAYSCALE)
      img = cv.resize(img, (WIDTH*2, int(attachment.height/attachment.width*WIDTH))) 

      img_str = ""
      for row in img:
        for col in row:
          img_str += " .,-~:;=!*#$@"[int(col/20)]
        img_str += "\n"

      try:
        for i in range(0, len(img_str), (WIDTH*2+1)*16):
          chunk = img_str[i:i + (WIDTH*2+1)*16]
          await ctx.send("```" + chunk + "```")
      except discord.errors.HTTPException as error:
        await ctx.send(error)
