def binary_search(list, target):
    middle = 0
    start = 0
    end = len(list)
    step = 0

    while(start<=end):

        print(f"steps =: {step} : {str(list[start:end+1])}")

        step = step + 1
        middle = (start + end) // 2
 
        if target == list[middle]:

            return middle

        if target < list[middle]:
            end = middle -1
        
        else:
            start = middle + 1
    
    return -1

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
targetnum = 12
binary_search(numbers, targetnum)
