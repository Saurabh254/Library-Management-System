# from .factory import logger
import glob
import os

def Code_length():
    length = 0
    for files_folders in glob.glob(pathname="D:/codes/Library-Management-System/*"):
        if os.path.isfile(files_folders):
            if files_folders.endswith(".py"):
                with open(files_folders) as f:
                    length += len(f.readlines())
        elif os.path.isdir(files_folders):
            for files in glob.glob(pathname=f"{files_folders}/*"):
                if files.endswith(".py"):
                    with open(files) as f:
                        length += len(f.readlines())
    return length


if __name__ == '__main__':
    try:
        length = Code_length()
        print(length)
    except Exception as E:
        # logger.error()
        pass