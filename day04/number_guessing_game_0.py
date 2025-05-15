import random
secret_number = random.randint(1, 20)
guess_str = input("Guess a whole number between 1 and 20: ")
guess = int(guess_str)

if guess == secret_number:
    print("Congratulations! You guessed the number!")
elif guess < secret_number:
    print("Your guess is smaller than the secret number.")
else:
    print("Your guess is bigger than the secret number.")
