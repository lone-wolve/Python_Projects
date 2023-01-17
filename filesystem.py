import os
#get current working directory
def get_curren_directory():
    cwd = os.getcwd()
    print("your current working directoty is ", cwd)

def change_directory():
    chdir = os.chdir("../")
    print("your changed directoty to ",  chdir)

def scan_directory(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            print(entry)


get_curren_directory()
change_directory()
get_curren_directory()
scan_directory("Tester1/")