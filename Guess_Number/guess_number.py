import random

def guess_number():
    print("Welcome to the Game!")
    print("Try to guess the number between 1 and 100.")
    number = random.randint(1, 100)
    step = 1

    while True:
        user_input = input("Enter a number: ")
        if not user_input.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue

        user_number = int(user_input)
        if not (1 <= user_number <= 100):
            print("Number out of range. Please enter a number between 1 and 100.")
            continue

        if user_number == number:
            print(f"Well done! You guessed the correct number {number} in {step} steps.")
            break
        elif user_number < number:
            print(f"Step {step}: The number is bigger than {user_number}. Try again.")
        else:
            print(f"Step {step}: The number is smaller than {user_number}. Try again.")

        step += 1

guess_number()
