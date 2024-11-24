import random
from random import choice


def hangman(strings_list):
    hidden_word = choice(strings_list).lower()
    chance = random.randint(5, 10)
    temp_chance = chance
    guessed_letters = set()

    print("Welcome to Hangman!")
    print("Guess the word!")
    print(f"You have {chance} chances to guess the word.")
    print(f"The word has {len(hidden_word.replace(' ', ''))} letters (ignoring spaces).\n")

    word = list(hidden_word)
    display = ["_" if char != " " else " " for char in word]
    print(" ".join(display), "\n")

    while chance > 0:
        guess = input("Enter your guess (a single letter): ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single alphabetical character.\n")
            continue

        if guess in guessed_letters:
            print("You already used that letter! Try a different one.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
            print("Correct!", " ".join(display), "\n")
        else:
            chance -= 1
            print(f"Incorrect! You have {chance} chances left.\n")
            print(" ".join(display), "\n")

        if display == word:
            print(f"Congratulations! You guessed the word: '{hidden_word}' in {temp_chance - chance} chances! \n")
            break

    if chance == 0:
        print(f"You've run out of chances! The word was '{hidden_word}'.\n")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        hangman(strings_list)
    else:
        print("Thank you for playing Hangman!\n")


lst = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "fruit salad",
    "blackberry pie", "dragon fruit", "green apple", "chocolate cake", "summer breeze"
]

hangman(lst)
