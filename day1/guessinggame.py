import random


def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess(1-100) : "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess < target_number:
            print("Too low. Try again.")
        elif guess > target_number:
            print("Too high, Try again")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    play_again = input("Do you want to play again? (yes/no) : ").lower()
    return play_again == "yes"


while play_game():
    pass

print("Thanks for playing!")
