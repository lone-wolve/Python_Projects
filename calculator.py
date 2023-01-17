def add(a, b):
    answer = a+b
    print(f"{a} + {b} = {answer}\n")


def subtract(a, b):
    answer = a - b
    print(f"{a} - {b} = {answer}\n")

def multiplication(a, b):
    answer = a * b
    print(f"{a} * {b} = {answer}\n")

def division(a, b):
    answer = a/b
    print(f"{a} / {b} = {answer}\n")


while True:

    print("Welcome to the calculator")                                                                                          
    info = "follow instructiontion below to perform anyy calcultion\nA-->for addition\nS-->for Subtraction\n"
    print(info)

    choice = input("enter a your choice to perform any operation----> ")

    if choice == "A" or choice == 'a':
        a = int(input("enter Num1----> "))
        b = int(input("enter Num2----> "))
        print(" ")
        add(a,b)
    elif choice == "S" or choice == 's':
        
        a = int(input("enter Num1----> "))
        b = int(input("enter Num2----> "))
        subtract(a,b)
    
    elif choice == "D" or choice == 'd':
        
        a = int(input("enter Num1----> "))
        b = int(input("enter Num2----> "))
        division(a,b)
    

    elif choice == "M" or choice == 'm':
        
        a = int(input("enter Num1----> "))
        b = int(input("enter Num2----> "))
        multiplication(a,b)
        

    elif choice == "q" or choice == "Q":
        quit()
