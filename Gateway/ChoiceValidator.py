def Validator(choice: str):
    if not choice.isdigit():
        if choice in ['q', 'Q', 'close','quit']:
            quit()
    if choice.isdigit() and len(choice) == 1:
        