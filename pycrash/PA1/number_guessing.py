import random
import math


print("Number Guessing Game. Choose a upper and lower bound.")  

low = int(input("Lower Bound: "))
high = int(input("Higher Bound: "))

#so i dont make a nested list like li_int = list(range(low, high + 1))
li_int = [i for i in range(low, high + 1)]

ran_num = random.randrange(low, high)

guess = 0
guess_total = 0

def binary_search(lst, target):
    high = len(lst) - 1
    low = 0
    num_guess = 0

    while low <= high:
        mid = (high + low) // 2
        num_guess += 1

        if lst[mid] < target:
            low = mid + 1
            num_guess += 1
        
        elif lst[mid] > target:
            high = mid - 1
            num_guess += 1
        
        elif lst[mid] == target:
            return num_guess

        else:
            pass
        
    return -1

guess_total = binary_search(li_int, ran_num)

print(f"You have {guess_total} guesses.")
a1 = ""

while a1 != ran_num:
    a1 = int(input("Enter your Guess: "))

    if a1 > ran_num:
        print("Guess too high")
        guess_total -= 1
        print(f"You have {guess_total}s remaining")

    elif a1 < ran_num:
        print("Guess is too low")
        guess_total -= 1
        print(f"You have {guess_total}s remaining")

    else:
        print("Correct Guess, Hurrah")

    



