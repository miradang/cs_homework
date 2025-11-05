import random
import math


print("Number Guessing Game. Choose a upper and lower bound.")  

low = int(input("Lower Bound: "))
high = int(input("Higher Bound: "))

li_int = list(range(low, high + 1))

ran_num = random.randrange(low, high)

guess = 0
guess_total = 0

def binary_search(lst, target):
    
    
    high = len(lst) -1
    low = 0
    mid = (high + low) // 2
    num_guess = 0

    while low <= high:
        if lst[mid] < target:
            low = mid + 1
            num_guess += 1
        
        elif lst[mid] > target:
            high = mid - 1
            num_guess += 1
        else:
            return num_guess
    return -1

guess_total = binary_search([li_int], (ran_num))

print(guess_total)



