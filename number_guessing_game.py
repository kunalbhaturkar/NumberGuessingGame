import random

print("=== Number Guessing Game ===")
number = random.randint(1, 100)
attempts = 0
guess = 0

while guess != number:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")