from typing import Union

def Validator(choice: str, choiceLimit=None) -> Union[int, None]:
    if not choice.isdigit():
        if choice in ['q', 'Q', 'close','quit']:
            quit()
    if choice.isdigit():
        choice = int(choice)
        if choiceLimit is None:
            return False
        if 0 < choice <= choiceLimit:
            return choice 
    else:
        return None




