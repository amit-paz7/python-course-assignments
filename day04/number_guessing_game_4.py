import random
secret_number = random.randint(1, 20)
debug_mode = False
while True:
    if debug_mode:
        print(f"(Debug Mode) The secret number is: {secret_number}")
    guess_str = input("Guess a whole number between 1 and 20 (or 'x' to exit, 's' for secret, 'd' for debug): ")
    if guess_str.lower() == 'x':
        print("Exiting the game.")
        break
    elif guess_str.lower() == 's':
        print(f"The secret number is: {secret_number}")
        continue
    elif guess_str.lower() == 'd':
        debug_mode = not debug_mode
        if debug_mode:
            print("Debug Mode is now on.")
        else:
            print("Debug Mode is now off.")
        continue
    try:
        guess = int(guess_str)
        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break
        elif guess < secret_number:
            print("Your guess is smaller than the secret number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 20, or a command ('x', 's', 'd').")
        else:
            print("Your guess is bigger than the secret number. Try again.")
   
