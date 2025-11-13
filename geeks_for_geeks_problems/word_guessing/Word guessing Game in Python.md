Word guessing Game in Python

This program is a simple word-guessing game where the user has to guess the characters in a randomly selected word within a limited number of attempts. The program provides feedback after each guess, helping the user to either complete the word or lose the game based on their guesses.
2. Getting the User's Name, and Greeting the User

The program asks the user for their name using the input() function. This name is stored in the variable name.
3. List of Words and Choosing a Random Word

A list of possible words for the guessing game is defined. These words are strings stored in a list called words. Also, the program selects a random word from the words list using random.choice(). The selected word is stored in the variable word.
4. Prompting the User to Guess

The program prompts the user to start guessing the characters of the randomly chosen word.
5. Initializing Guesses and Turns

    guesses: An empty string that will hold all the characters guessed by the user.
    turns: The number of attempts the user has to guess the word. Initially set to 12.
    6. The Main Game Loop

This while loop runs as long as the user has remaining turns. Inside the loop, the user will be prompted to guess characters.

while turns > 0:

6.1. Checking Each Character in the Word

    failed = 0: A counter for the number of characters that have not been correctly guessed.
    The for loop iterates through each character in the word.
    If the character has been guessed (i.e., it is in guesses), it is displayed.
    If the character has not been guessed, an underscore (_) is displayed, and failed is incremented.

6.2. Checking if the User Has Won

If failed is 0, it means all characters in the word have been guessed correctly. The user wins, and the correct word is displayed. The game ends with a break statement.
6.3. Prompting for the Next Guess

    The user is prompted to guess a character.
    The guessed character is added to the guesses string.
    6.4. Handling Incorrect Guesses

    If the guessed character is not in the word, the number of turns decreases by 1.
    A "Wrong" message is displayed, along with the number of remaining guesses.
    6.5. Checking if the User Has Lost

If the user runs out of turns, the game ends with a "You Lose" message.
7. Ending the Game

    The game loop will end either when the user guesses the word correctly (all characters are guessed) or when the user runs out of turns.