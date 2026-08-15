# Number Guessing Game

secret_number = 7
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations!")
        print("You guessed the number in", attempts, "attempts.")
        break