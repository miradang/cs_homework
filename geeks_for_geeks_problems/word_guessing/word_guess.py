import random

name = input("Write your name here: ")

word_list = ["apple", "book", "desk", "pen", "cat", "dog", "tree", "house", "car", "phone",
             "computer", "laptop", "keyboard", "mouse", "chair", "table", "door", "window", "wall", "floor"]

word_guess = random.choice(word_list)

word_len = len(word_guess)

turns = word_len + 5

incorrect = ""
correct = ""


print(f"You have {turns} turns")

print(word_guess)

guess_char = input("Guess a character: ")

while turns > 0:
    
    if guess_char in word_guess:
        correct += guess_char
        turns -= 1
        print(f"You have guessed correct {guess_char} is in the word. You have {turns} remaining")
        print(f"you have guessed incorrectly {incorrect} and {correct} correctly")
        guess_char = ""
        guess_char = input("Guess a character: ")
    
    elif sorted(correct) == sorted(word_guess):
        print("You have won")
        turns -= 100
        break


    else:
        turns -= 1
        incorrect += guess_char
        print(f"{guess_char} is not in that word.  You have {turns} remaining")
        print(f"you have guessed incorrectly {incorrect} and {correct} correctly")
        guess_char = ""
        guess_char = input("Guess a character: ")

else:
    print("You have lost")





