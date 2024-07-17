import random
from hangman_art import logo, stages
from hangman_words import word_list

word_list_len = len(word_list) - 1
chosen_word = word_list[random.randint(0, word_list_len)]
# print(f'Pssst, the solution is {chosen_word}.')

match = False
lives = 6
display = []
for letters in chosen_word:
    display.append("_")
guessed_before = []

print(logo)
while match == False:
    guess = input(f'Guess a letter. \nLives: {lives}\nLetter: ').lower()
    guessed_before.append(guess)

    l = -1
    for letter in chosen_word:
        l += 1
        if letter == guess:
            display[l] = letter

    c = guessed_before.count(guess) - 1

    if guess in chosen_word:
        print(f"Nice! You have ({lives}) lives left.\n{stages[lives]}")
    elif c > 0 and not guess in chosen_word:
        print(f"You have used that letter before.\nYou have {lives} lives remaining.\n{stages[lives]}")
    elif not guess in chosen_word:
        lives -= 1
        print(f"That letter is not in the word.\nYou have {lives} lives remaining.\n{stages[lives]}")
        if lives == 0:
            print(f"\nYou Lose.\n\nWord was: {chosen_word}")
            match = True

    print(f"{' '.join(display)}\n")
    if "_" not in display:
        match = True
        print(f"You Win!\n\n{stages[lives]}")