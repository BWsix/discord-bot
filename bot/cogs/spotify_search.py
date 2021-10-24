import requests
from jsonpath_ng import parse

from discord.ext import commands

SPOTIFY_API = "https://spotify-api-vflc.vercel.app/api/"
TYPES = ["albums", "artists", "tracks", "playlists", "shows", "episodes"]

class Spotify_Search(commands.Cog): 
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    
  @commands.command(name="search")
  async def search(self, ctx: commands.Context, *query):
    res = requests.get(SPOTIFY_API + f"search/{' '.join(query)}")
    res_json = res.json()

    all_results = []
    
    for t in TYPES:
      jexp_has_result = parse(f"$.{t}.total")
      result = jexp_has_result.find(res_json)[0].value

      if not result:
        continue

      jexp_get_url = parse(f"$.{t}.items[0].external_urls.spotify")
      url = jexp_get_url.find(res_json)[0].value

      all_results.append((t, url))

    if not all_results:
      return await ctx.send("not found.")
      
    for t, url in all_results:
      await ctx.send(f"found {t[:-1]}:\n{url}")
