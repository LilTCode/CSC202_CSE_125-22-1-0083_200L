
import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Put a letter: ").lower()

    if guess in display:
        print(f"You've guessed {guess} already, try another.")

    for position in range(word_length):
        letter = chosen_word[position]
     
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:

        print(f"You guessed {guess}, the word is not found. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")





