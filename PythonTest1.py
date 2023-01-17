def check_largest_number(values:list):
    lowest = min(values)
    largest = max(values)
    print(f"The lowest number is {lowest}\nThe largest number is {largest}")

storage = []
while True:
    try:
        userInput = input("enter a number\n---->")
        if userInput == "done":
            break
        userInput = int(userInput)
        storage.append(userInput)
    except ValueError as error:
        print(f"{error}")
        
print(f"The numbers you enters are {storage}")
check_largest_number(storage)



