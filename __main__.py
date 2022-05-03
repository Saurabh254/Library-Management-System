from ctypes import Union
from .factory import (
    logger,
    TermStyles,
)
from time import sleep
from . import conn
from . import cur
from tqdm import tqdm
import os
from .utils import cleaner
from .Gateway import Validator

while True:
    cleaner()
    HomepageChoice: str = input(TermStyles.homepage)
    Choice = Validator(choice=HomepageChoice, choiceLimit=4)
    if Choice is not None or Choice == False:
        if Choice:
            Choice = int(Choice)
            break
        else:
            print("limit excedded")
            pass
    else:
        print("Enter choice in proper format")
    print()

    print("RESTARTING...")
    for i in tqdm(range(5)):
        sleep(1)

    

print(Choice)
