
# ====================================================        __init__.py        ==============================================================

"""
 Brief Detail of __init__.py

 database handler: conn (connection), cur (cursor)
 setup of cursor and connection is been done within Miscellaneious
 Global import has been intiated here
"""
# -------------------------------------------------        Importing Modules        -----------------------------------------------------------

from .DBConnector import Connector

from ..factory import logger

from ..factory import PsqlError

# --------------------------------------------------------        Miscellaneous        -----------------------------------------------------------

# Calling Connection function and assigning cursor to cur for sql executions.

conn = None
cur = None

try:

    conn = Connector().connectionfunc()
    cur = conn.cursor()
    conn.autocommit = True

except Exception as E:

    logger.warning(
        f"{__name__} # {PsqlError(E)}"
    )


# ------------------------------------------------------        Importing setup        ------------------------------------------------------------

# for Global import

__all__ = [
    cur,
    conn,
]

# ------------------------------------------------------      End of __init__.py      --------------------------------------------------------
