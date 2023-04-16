# -----------------------------------------------------------
# Import modules
# -----------------------------------------------------------
# API Telegram bot
import telebot
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
# Message in terminal
from bot.bot import GrammarBot
# in folder tools: server/system.py
from tools.server.system import server_stop

if __name__ == "__main__":
    # add key bot.
    grammar_bot = telebot.TeleBot('5829614461:AAF-PiVBoAyinjm4B_qdHwCVcQ0qD_P7wsQ')
    # create bot as class
    grammar_def: GrammarBot = GrammarBot()
    # add function's bot.
    # list get functions in file: bot/bot.py
    grammar_def.functions(grammar_bot)
    # run bot
    # view logo in terminal
    grammar_bot = GrammarBot.run(grammar_def,grammar_bot)
    # stop bot
    # view logo in terminal
    server_stop()


