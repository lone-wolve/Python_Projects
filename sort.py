def sort(A):
    for i in range (0, len(A)):

        current = A[i]

        position = i

        current_pos = A[position-1]

        print(f"current = {current}\nposition = {position}\ncurrent position = {current_pos}\n*************")

array = [3,4,9,0,7,6,1,5,2]
sort(array)