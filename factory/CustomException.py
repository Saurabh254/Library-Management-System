class PsqlError(Exception):
    '''Could not connect to the database'''


class SqlCodeError(Exception):
    '''There is an error in your Sql Code'''

class KwargsError(Exception):
    '''Wrong Keyword argument has been passed'''


class PathError(Exception):
    '''Invalid path has been specified'''

class TerminalClearError(Exception):
    '''Failed to clear up the terminal'''