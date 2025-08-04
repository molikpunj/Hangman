'''SIMPLE HANGMAN GAME!!!'''

import random

attempts = 15
words = ["feline", "tiger", "country", "prosperous", "terrific", "anonymous", "explode", "surface", "supervise", "conscious"]

def maingame():
    chosen_word = random.choice(words)
    display = ["_" for _ in chosen_word]
    print(display)

print("Welcome To Hangman!")
maingame()