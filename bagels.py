"""
Bagels a deductive guessing game where you guess a number based on clues.
Tags: Short, game, puzzle
"""

import random

NUM_DIGITS = 3  # number of digits, try 1 to 10
MAX_GUESSES = 10  # maximum number of guesses try 1 - 100


def main():
    print(
        """
Bagels, a deductive guessing game where you guess a number based on clues.
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is.

Here are the clues:
  * Pico   One digit is correct but in the wrong position.
  * Fermi  One digit is correct and in the right position.
  * Bagels No digit is correct.
"""
    )

    while True:
        # Generate a secret number with uniques digits.
        secret_num = get_secret_num()

        print("I have thought up a number.")
        print("You have {} guesses to get it.".format(MAX_GUESSES))

        num_guesses = 1

        while num_guesses <= MAX_GUESSES:
            guess = ""
            # Ensure valid guesses (correct number of digits)

            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(num_guesses))
                guess = input("> ")

            clues = get_clues(guess, secret_num)
            print(clues)

            if guess == secret_num:
                break

            num_guesses += 1

        if num_guesses > MAX_GUESSES:
            print("You ran out of guesses")
            print("The anser was {}".format(secret_num))

        # Ask if they want to play again(case -sensitive)
        print("Do you want to play again? (yes/no)")
        play_again = input("> ").lower()
        if not play_again.startswith("y"):
            break
    print("Thank you for playing!")


def get_secret_num():
    """Return a string representing a secret number with unique digits."""
    numbers = list("0123456789")  # Create a list of digits 0-9
    random.shuffle(numbers)  # Shuffle digits randomly

    secret_num = ""
    # Ensure unique digits using a set
    unique_digits = set()
    while len(unique_digits) < NUM_DIGITS:
        digit = random.choice(numbers)
        if digit not in unique_digits:
            unique_digits.add(digit)
            secret_num += str(digit)

    return secret_num


def get_clues(guess, secret_num):
    """Return a string with Pico, Fermi, Bagels clues for a guess-secret pair."""
    if guess == secret_num:
        return "You got it!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")  # Correct digit in the correct place.
        elif guess[i] in secret_num:
            clues.append("Pico")  # Correct digit in the wrong place

    if len(clues) == 0:
        return "Bagels"  # No correct digits

    # Sort cluess alphabetically (Optional: hides positional information)
    clues.sort()
    return " ".join(clues)


# Run the game if the script is executed directly
if __name__ == "__main__":
    main()
