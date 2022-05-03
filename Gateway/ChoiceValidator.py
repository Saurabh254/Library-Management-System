from typing import Union

def Validator(choice: str, choiceLimit=None) -> Union[int, None]:
    if not choice.isdigit():
        if choice in ['q', 'Q', 'close','quit']:
            quit()
    if choice.isdigit() and len(choice) == 1:
        if choiceLimit is None:
            return False
        if 0 < int(choice) <= choiceLimit:
            return int(choice) 
    else:
        return None




