import random
from hangman_art import stages, logo
from words import word_list

import os

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []

for _ in range(word_length):
    display += "_"

print(f"Word have this options letters: {' '.join(display)}")

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    os.system('clear')

    if guess in display:
        print(f"You've already guessed {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print(f'The word is {chosen_word}\n')
            print("You lose.")
    if not "_" in display:
        game_is_finished = True
        print("You win.")
    print(stages[lives])