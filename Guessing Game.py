import random

def guess_the_number():
    min = 0
    max = 100
    the_number = random.randint(min, max)
    num_guesses = 0
    user_number = None

    while user_number != the_number:
        try:
            user_number = int(input(f"Guess a number between {min} and {max}: "))
            num_guesses += 1  # Increment attempts on each guess

            if user_number > the_number:
                print("Too high! Try again.")
            elif user_number < the_number:
                print("Too low! Try again.")
        except ValueError:
            print('ERROR: Invalid input. Please enter an integer.')
            user_number = None

    print(f"YOU DID IT! {the_number} was the correct number. You guessed it in {num_guesses} attempts!")

if __name__ == "__main__":
    guess_the_number()
