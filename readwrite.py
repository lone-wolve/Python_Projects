def read_from_file():

    with open('text.txt', 'r') as f:
        read_mode = f.read(10)
        read_line = f.readlines()
        print(read_mode)
        print(read_line)

def read_from_file_write():

    with open('text.txt', 'w') as f:
        f.write('lorem ipsum today is a wondeful day i can''t swiim ')

read_from_file_write()
read_from_file()

