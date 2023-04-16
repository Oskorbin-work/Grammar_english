# -----------------------------------------------------------
# Import classical modules
# -----------------------------------------------------------
import time
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
# wrapper for different status message (ok, warning, error, etc)
from tools.developments.wrapper import Wrapper


class TerminalTime:
    """
    Class for time message
    """
    def __init__(self, kind):
        """
        :param time_kind: kind message. What it is.
        """
        self.kind = kind
        self.time_now = self.time_set()

    def time_set(self):
        """
        :return: now time
        """
        sec = time.time()
        struct = time.localtime(sec)
        result = time.strftime('%d %b %y %H:%M:%S ', struct)
        return result

    def wrapper(self):
        """
        :return: message + format message
        """
        if self.kind == "success":
            return Wrapper(self.time_now).ok()
        if self.kind == "fail":
            return Wrapper(self.time_now).fail(False)
        else:
            return Wrapper(self.time_now).common()+ Wrapper("Kind time is wrong :").warning()

    def time_get(self):
        """
        :return: time + format message
        """
        return self.wrapper()