from datetime import datetime
import os

def formatDatetime(timestamp):
    utc_timesamp = datetime.utcfromtimestamp(timestamp)
    formatedDate = utc_timesamp.strftime("%d %b %Y %H %M %S")
    return formatedDate


def get_curren_directory():
    cwd = os.getcwd()
    print("your current working directoty is ", cwd)


def change_directory():
    chdir = os.chdir("../")
    print("your changed directoty to ",  chdir)

def displayfile(directroy):
    with os.scandir(directroy) as entries:
        for entry in entries:
            if entry.is_file():
                print("file Name ", entry)

def displayfolder(directroy):
    with os.scandir(directroy) as entries:
        for entry in entries:
            if entry.is_dir():
                print("Directory Name ", entry)

# def scandir(directory):
#     with os.scandir(directory) as entries:
#         for entry in entries:
#             print("Name ",entry.name)
#             info  = entry.stat()
#             print("creation time ", formatDatetime(info.st_ctime))

#             print("last accesed  time ", formatDatetime(info.st_atime))

#             print("file size ", info.st_size)

get_curren_directory()
change_directory()
displayfolder("fast_api_project2/")
displayfile("fast_api_project2/")
# scandir("Tester1/")

