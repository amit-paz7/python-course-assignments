import random
secret_number = random.randint(1, 20)
while True:
    guess_str = input("Guess a whole number between 1 and 20 (or 'x' to exit): ")
    if guess_str.lower() == 'x':
        print("Exiting the game.")
        break
    try:
        guess = int(guess_str)
        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break
        elif guess < secret_number:
            print("Your guess is smaller than the secret number. Try again.")
        else:
            print("Your guess is bigger than the secret number. Try again.")
