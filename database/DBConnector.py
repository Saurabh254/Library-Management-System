

# ====================================================       DBConnector.py        ==============================================================

'''
Brief Detail of DBConnector.py

 database handler: conn (connection), cur (cursor)
 psycopg2 is used as a connector.
 database parameters are secured as environment variables with decouple.
'''

# -------------------------------------------------        Importing Modules        -----------------------------------------------------------

# importing psycopg2 for connecting python with postgres.
# To Install psycopg2 using pip use command 'pip install psycopg2'
import psycopg2

# imported logger for creating a logging file.
# logger setup can be found under Library-Management-System/factor/logger.py
from ..factory import logger

# Inbuild function typing
from typing import Callable

# Imported decouple for accessing environment variables
from decouple import config


# -------------------------------------------------        Environment Variables        -------------------------------------------------------
class EnvironmentPara:
    Database: str = config("Database")
    User:     str = config("User")
    Password: int = config("Password")
    Host:     str = config("Host")
    Port:     int = config("Port")
# -------------------------------------------------------        Functions        -------------------------------------------------------------

# connection function for accessing database


class Connector(EnvironmentPara):

    def __init__(self) -> None:
        super().__init__()

    def connectionfunc(self) -> Callable:

        '''
        Function name: connectionfunc
        Returns psycopg2 connection as conn
        '''

        # With clause is used to escape from closing the connection

        with psycopg2.connect(
            database  =  self.Database,
            user      =  self.User,
            password  =  self.Password,
            host      =  self.Host,
            port      =  self.Port,
        ) as conn:

            return conn

# ----------------------------------------------- --         End of DBConnector.py         ---------------------------------------------------