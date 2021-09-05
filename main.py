from os import environ
from bot.bot import run

if __name__ == "__main__":
  run(environ.get("BOT_TOKEN"))
