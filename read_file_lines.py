# from .factory import logger
from glob import glob
import os

def main(path = None, length: int = 0): 
    if path is not None:
        for files_folder in glob(f'{path}/*'):
            if os.path.isfile(files_folder) and files_folder.endswith(".py"):
                with open(file=files_folder,  encoding="utf8") as f:
                    length += len(f.readlines())
                
            if os.path.isdir(files_folder):
                length += main(path=files_folder)   
        else:
            return length


if __name__ == '__main__':
    try:
        
        print(main(path='D://codes/PasslockDesktop'))
        # length = main("Trinity")
        # print(length)
    except Exception as E:
        print(E)