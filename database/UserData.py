from . import cur, conn
from ..factory import logger
from ..factory import SqlCodeError, KwargsError


class UserInfo:

    columns = [
        'IdentityNum',
        'first_name',
        'middle_name',
        'last_name',
        'gender',
        'dob'
    ]

    def IdExtractor(self, IdentityNum=None):

        if id != None:

            cur.execute(
                f'''SELECT IdentityNum,
                first_name,
                middle_name,
                last_name,
                gender,
                dob
                FROM LibManageSys
                WHERE IdentityNum = {IdentityNum}'''
            )

            IdentityNum, first_name, middle_name, last_name, gender, dob = cur.fetchall()[
                0]

    def update(
        self,
        IdentityNum=None,
        **kwargs
    ):

        wrong_arguments = False

        for i in kwargs.keys():

            if i not in self.columns:
                wrong_arguments = True
                break

        if wrong_arguments:
            return None

        Parameter = []
        for i in kwargs.keys():

            Parameter.append(f"{i} = '{kwargs[i]}'")

        try:
            cur.execute(
                f"UPDATE person SET {', '.join(Parameter)} WHERE id = {IdentityNum}"
            )
            return True

        except Exception as E:
            return False
