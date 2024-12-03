import random
from random import choice


def load_words():
    with open("words.txt", "r") as file:
        words_ = [line.strip().split(",", 1) for line in file]
    return words_


def hangman(words_list):
    word, hint = choice(words_list)
    hidden_word = word.lower().strip()
    chance = random.randint(5, 10)
    temp_chance = chance
    guessed_letters = set()

    print("Welcome to Hangman!")
    print("Guess the word!")
    print(f"You have {chance} chances to guess the word.")
    print(f"The word has {len(hidden_word.replace(' ', ''))} letters.\n")

    print(f"Hint: {hint}\n")

    word = list(hidden_word)
    display = ["_" if char != " " else " " for char in word]
    print(" ".join(display), "\n")

    while chance > 0:
        guess = input("Enter your guess (a single letter or the whole answer): ").lower().strip()

        if len(guess) == 1 and guess.isalnum():
            if guess in guessed_letters:
                print("You already used that character! Try a different one.\n")
                continue
            guessed_letters.add(guess)

            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        display[i] = guess
                print("Correct!\n")
                print(" ".join(display), "\n")
            else:
                chance -= 1
                print(f"Incorrect! You have {chance} chances left.\n")
                print(" ".join(display), "\n")

        elif len(guess) > 1:
            if guess == hidden_word:
                print(f"Congratulations! You guessed the word: '{hidden_word}' in {temp_chance - chance} tries! \n")
                break
            else:
                print(f"Incorrect guess! You lose. The word was '{hidden_word}'.\n")
                break
        else:
            print("Invalid input! Please enter a single character or the whole answer.\n")

        if display == word:
            print(f"Congratulations! You guessed the word: '{hidden_word}' in {temp_chance - chance} tries! \n")
            break

    if chance == 0 and display != word:
        print(f"You've run out of chances! The word was '{hidden_word}'.\n")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        hangman(words_list)
    else:
        print("Thank you for playing Hangman!\n")


words = load_words()
hangman(words)
