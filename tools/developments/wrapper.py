# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
# get all colour for terminal
from tools.text.text_colour import bcolors


class Wrapper:
    """
    class for different status message (ok, warning, error, etc)
    """
    def __init__(self, text):
        """
        :param text: text which it is must wrapper
        """
        self.text = text

    def warning(self, with_info = True):
        """
        :param with_info: True -- if need label "WARNING"
        :return: data with colour if warning
        """
        if with_info:
            return bcolors.WARNING + "WARNING: !* " + self.text + " *!\t" + bcolors.ENDC
        else:
            return bcolors.WARNING + self.text + "\t" + bcolors.ENDC

    def ok(self, with_info = True):
        """
        :param with_info: True -- if need label ...
        :return: data with colour if good working
        """
        if with_info:
            return bcolors.OKGREEN + self.text + "\t" + bcolors.ENDC
        else:
            return bcolors.OKGREEN + self.text + "\t" + bcolors.ENDC

    def fail(self,with_info = True):
        """
        :param with_info: True -- if need label "FAIL"
        :return: data with colour if get error
        """
        if with_info:
            return bcolors.FAIL + "FAIL: !!! " + self.text + " !!!\t" + bcolors.ENDC
        else:
            return bcolors.FAIL + self.text + "\t" + bcolors.ENDC

    # text without wrapper
    def common(self, with_info=True):
        """
        :param with_info: True -- if need label ....
        :return: data without colour
        """
        if with_info:
            return self.text
        else:
            return self.text