# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
# set time for every message
from terminal.time.time import TerminalTime
# wrapper for different status message (ok, warning, error, etc)
from tools.developments.wrapper import Wrapper


class TerminalMessage:
    """
    class for message in the terminal
    """
    def __init__(self, message, kind):
        """
        :param message: text message
        :param kind: kind message. What it is.
        """
        self.message = str(message)
        self.kind = kind
        self.wrapper()

    def wrapper(self):
        """
        add wrapper for message
        """
        if self.kind == "success":
            pass
        elif self.kind == "fail":
            self.message = Wrapper(self.message).fail()
        else:
            self.message = Wrapper("Kind message is wrong").warning()

    def print(self):
        """
        print message in the terminal
        """
        print(TerminalTime(self.kind).time_get() + self.message)


