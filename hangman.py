from Random_Words import my_list
import random

word = random.choice(my_list)

guessed = []  # empty list to store all correct guesses
wrong = []  # empty list to store all incorrect guesses
alphabet = "abcdefghijklmnopqrstuvwxyz"  # string to verify only lowercase english letters are entered
tries = 8

print("H A N G M A N")

user_choice = input("Type 'play' to play the game: ")
if user_choice == "play":
    while tries > 0:
        display = ""
        for letter in word:
            if letter in guessed:
                display = display + letter
            else:
                display = display + "-"

        if tries > 0 and display == word:
            print("You survived!")
            break

        print()
        print(display)
        guess = input("Input a letter: ")

        if len(guess) > 1:  # ensures only a single character is inputted
            print("You should input a single letter")
        elif guess not in alphabet:  # ensures only english letters are inputted
            print("Please enter a lowercase English letter")
        elif guess in guessed or guess in wrong:  # repeated entries will display a warning
            print("You've already guessed this letter")
        elif guess in word:
            guessed.append(guess)  # adds the correctly guessed letter to the 'guessed' list
        else:  # if the letter is incorrect this block runs
            print("That letter doesn't appear in the word")
            tries = tries - 1  # takes away a try
            wrong.append(guess)  # adds the incorrectly guessed letter to the 'wrong' list
    else:  # if the player has no more tries and haven't guessed the word
        print("You lost!")
else:  # if anything other than 'play' is entered the game won't run
    print()