import random


def guess_number():
    print("\nWelcome to the Game!")
    print("Try to guess the number between 1 and 100.")

    ans = input("Do you want to play? (yes/no): ")
    if ans.lower() == "no":
        print("Goodbye!")
        exit()
    else:
        print("Let's start!\n")

    number = random.randint(1, 100)
    step = 1

    while True:
        user_input = input("Enter a number: ")
        if not user_input.isdigit():
            print("Invalid input. Please enter a valid number.\n")
            continue

        user_number = int(user_input)
        if not (1 <= user_number <= 100):
            print("Number out of range. Please enter a number between 1 and 100.\n")
            continue

        if user_number == number:
            print(f"Well done! You guessed the correct number {number} in {step} steps.\n")
            break
        elif user_number < number:
            print(f"Step {step}: The number is bigger than {user_number}. Try again.\n")
        else:
            print(f"Step {step}: The number is smaller than {user_number}. Try again.\n")

        step += 1


while True:
    guess_number()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing. Goodbye!\n")
        break
