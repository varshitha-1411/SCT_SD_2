import random


def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 50. Can you guess it?")

    number_to_guess = random.randint(1, 50)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(
                    f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    guess_the_number()
