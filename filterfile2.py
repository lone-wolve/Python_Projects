import os
import glob

# def display_pngs():
#     pngFiles = glob.glob('*.txt')
#     print(pngFiles)

# def findSpecificFile():
#     filteredFile = glob.glob('*text01*')
#     print(filteredFile)

def findFileSubdir():

    for files in glob.iglob('**/*text01*', recursive=True):
        print(files)

def get_top_down_dir():

    for dirpaths,dirnames, files in os.walk('artwork/'):
            print(f"Directory path name: {dirpaths}")
            print(f"Included sub dicteory below")
            
            for dirname in dirnames:
                print(f"subdirectory  is {dirname} ")

            for file in files:
                print(file)   

            print()      


def get_down_top_dir():

    for dirpaths,dirnames, files in os.walk('artwork/', topdown=False):
            print(f"Directory path name: {dirpaths}")
            print(f"Included sub dicteory below")
            
            for dirname in dirnames:
                print(f"subdirectory  is {dirname} ")
                print("files below")

            for file in files:
                print(file)   

            print()      
            


## display_pngs()
# findSpecificFile()
# findFileSubdir()
get_top_down_dir()
get_down_top_dir()