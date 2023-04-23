# -----------------------------------------------------------
# Import modules
# -----------------------------------------------------------
# Tools for json
import json
# for json highlight in the terminal
from pygments import highlight, lexers, formatters
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
# Main Message in terminal
from terminal.message.main import TerminalMessage


class ChatUser(TerminalMessage):
    """
    TerminalMessage –– base for message in the terminal
    """

    def __init__(self, username, request, answer, kind):
        """
        :param username: user's username
        :param request: user's request
        :param answer: bot answer
        :param kind: kind message. What it is.
        """
        # -----------------------------------------------------------
        self.username = username
        self.request = request
        self.answer = answer
        # -----------------------------------------------------------
        self.message = self.data_to_message()
        self.kind = kind
        self.wrapper()

    def data_to_message(self):
        """
        :return: return data chat as message in the terminal (format as json)
        """
        def spec_symbols_to_format_json(text):
            special_symbol_python = ["\n"]
            special_symbol_json = ["\\n"]
            # replace special symbols.
            for x,y in zip(special_symbol_python, special_symbol_json):
                text = text.replace(x,y)
            return text

        def data_to_json_dumps():
            """
            :return: data chat how as json
            """
            json_data = '[{' \
                        '"Type_message": "Conversation with user and bot", ' \
                        f'"Username": "{self.username}",' \
                        f'"Request": "{self.request}",' \
                        f'"Answer": "{self.answer}"' \
                        '}]'
            json_data = spec_symbols_to_format_json(json_data)

            json_object = json.loads(json_data)
            dumps = json.dumps(json_object[0], indent=4, ensure_ascii=False)
            return dumps


        def json_dumps_to_message():
            """
            :return: json to message and add it highlight
            """
            dumps = data_to_json_dumps()
            result = highlight(dumps, lexers.JsonLexer(), formatters.TerminalFormatter())
            return result

        return json_dumps_to_message()
