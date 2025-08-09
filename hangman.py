'''SIMPLE HANGMAN GAME!!!'''

import random

words = ["feline", "tiger", "country", "prosperous", "terrific", "anonymous", "explode", "surface", "supervise", "conscious"]

def maingame():
    attempts = 15
    chosen_word = random.choice(words)
    display = ["_" for _ in chosen_word]
    while attempts > 0 and "_" in display:
        for _ in display:
            print(_, end = "")
        guess = input(" Guess one letter: ")
        if guess.lower() in chosen_word:
            print("Correct guess!")
            realguess = guess.lower()
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    display[i] = realguess
        else:
            print("Wrong guess!")
            attempts -= 1
            print(f"Remaining attempts: {attempts}")
    print("You win!")

print("Welcome To Hangman!")
maingame()