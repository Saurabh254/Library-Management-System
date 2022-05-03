
# =======================================================          Logger.py          ================================================================




import logging as logger



loggerfile = 'Library-Management-System/SystemError.log'

logger.basicConfig(
    filename='Library-Management-System/SystemError.log',
    filemode='a',
    level=logger.DEBUG,
    format='%(asctime)s: %(message)s ',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

__all__  = [logger]
