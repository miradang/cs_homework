import random
game = ''

while game != "n":

    print('Play a game of Rock, Paper, Scissors')
    print('Choose a item\n' \
    '1. Rock\n' \
    '2. Paper\n' \
    '3. Scissors\n')

    choice = int(input())

    while choice >= 3 or choice <= 0:
        valid_choice = 0
        if valid_choice == 0:
            choice = int(input('Please choose a number between 1 and 3: '))
    #actual input santization

    if choice > 3:
        print('Invalid Number. Choose a number between 1 and 3')
        choice = int(input())
        #bad attempt at input santization. if you enter in a invalid int here the program still crashes
    elif choice == 1:
        choice_name = "Rock"
        print('You selected Rock')
    elif choice == 2:
        choice_name = "Paper"
        print('You selected Paper')
    elif choice == 3:
        choice_name = "Scissors"
        print('You selected Scissors')
   

    comp_choice =  random.randint(1,3)

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissors"

    print(f'Computer selected {comp_choice_name}')

    if choice == comp_choice:
        result = "Draw"
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = "Rock"
        #rock beats scissors
    elif (choice == 2 and comp_choice == 1) or (choice == 1 and comp_choice == 2):
        result = "Paper"
        #paper beats rock
    elif (choice == 3 and comp_choice == 2) or (choice == 2 and comp_choice == 3):
        result = "Scissors"
        #scissors beats paper
    else:
        print('Decison loop invalid You shouldnt see this')
        break
    

    if result == 'Draw':
        print(f'DRAW\n You and the Computer both selected {choice}')
    elif result == choice_name:
        print(f'You Win\n You selected {choice_name} and the Computer selected {comp_choice_name}')
    else:
        print(f'You Lose\n You selected {choice_name} and the Computer selected {comp_choice_name}')

    print('Would you like to play again?')
    game = input("Y or N?")

print('Thanks for playing')    

