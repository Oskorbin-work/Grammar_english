# -----------------------------------------------------------
# Import modules
# -----------------------------------------------------------
import sys
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
# Main Message in terminal
from terminal.message.main import TerminalMessage


def server_stop():
    """
    When server shuts down
    """
    # if run successfully
    try:
        sys.exit(TerminalMessage("Stop bot...", "success").print())
    except Exception as e:
        sys.exit(TerminalMessage(f"Stop bot with error: {e}", "fail").print())


