# -----------------------------------------------------------
# Import modules
# -----------------------------------------------------------
# API Telegram bot
import telebot
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
# main message in the terminal
from terminal.message.main import TerminalMessage
# user's message in the terminal
from terminal.message.chat_user import ChatUser


class GrammarBot:
    """ Class for bot.
            It is storage function's bot
        grammar_bot (parameter's function ) is telebot. Create in file: main.py
    """
    # It is empty because it isn't having now
    def __init__(self):
        pass

    # run bot
    def run(self, grammar_bot):
        """
        :param grammar_bot: it is instance bot
        :return: turn on bot
        """
        # if run successfully
        try:
            TerminalMessage("Start bot...", "success").print()
            grammar_bot.polling(none_stop=True, interval=0)
        # if run has error
        except telebot.apihelper.ApiTelegramException:
            TerminalMessage("Api Telegram has error", "fail").print()
        return grammar_bot

    def functions(self, grammar_bot):
        """
        :param grammar_bot: it is instance bot
        """
        # When user begin to use bot
        @grammar_bot.message_handler(commands=['start'])
        def start(message):
            """
            :param message: it is data which print in the table
            """
            answer = "Hello from the system!"
            ChatUser(message.from_user.username,message.text,answer, "success").print()
            grammar_bot.send_message(message.from_user.id, answer)



