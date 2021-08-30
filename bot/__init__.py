from os import getenv
from bot.utils.repl_keep_alive import keep_alive

if getenv("REPL"):
  keep_alive()
