import os
from ..factory import (
    logger,
    TerminalClearError,
)

def cleaner():
    try:
        os.system("cls")
    except:
        try:
            os.system("clear")
        except Exception as E:
            logger.critical(TerminalClearError(E))



if __name__ == '__main__':
    cleaner()