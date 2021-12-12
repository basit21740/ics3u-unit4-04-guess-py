#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Dec 2021
# this program is number guessing game

from random import randint


def main():
    # this is function for creating guessing game

    # generating random number
    RANDOM_NUM = randint(0, 9)

    # Process , Input & Output
    while True:
        guess = input("Please guess a number: ")
        guess = int(guess)
        if guess == RANDOM_NUM:
            print(f"You guessed CORRECT 😎, the number is {RANDOM_NUM}")
            break
        print("Incorrect 🙁")
        print("Lets try again")

    # Done
    Print("\nDone.")


if __name__ == "__main__":
    main()
