# import os 
from pathlib import Path

# def creatdir1():
#     try:
#      os.mkdir('logout/')
    
#     except FileExistsError as ex:
#         print(f"log directory  already exist {ex}")

# def creatdir2():
#     dir_path = Path('output')
#     dir_path.mkdir(exist_ok= True)

# creatdir1()
# creatdir2()

def print_dir_content():
    
    entries = Path.cwd()

    for entry in entries.iterdir():
        print(entry.name)
        
        
