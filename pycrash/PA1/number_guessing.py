import random
import math


print("Number Guessing Game. Choose a upper and lower bound.")  

low = int(input("Lower Bound: "))
high = int(input("Higher Bound: "))

li_int = list(range(low, high))

ran_num = random.randrange(low, high)

guess = 0
guess_total = 0

def binary_search(array, target):
    
    high = array[-1]
    low = array[0]
    mid = (high + low) // 2

    while low <= high:
        if array[mid] < target:
            low = mid + 1
        
        elif array[mid] > target:
            high = mid - 1
        
        else:
            return mid
    return -1

guess_total = binary_search(li_int, ran_num)

print(guess_total)



