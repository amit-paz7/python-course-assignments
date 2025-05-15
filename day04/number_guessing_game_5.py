import random
secret_number = random.randint(1, 20)
debug_mode = False
move_mode = False
while True:
    if debug_mode:
        print(f"(Debug Mode) The secret number is: {secret_number}")
    guess_str = input("Guess a whole number between 1 and 20 (or 'x' to exit, 's' for secret, 'd' for debug, 'm' for move): ")
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
    elif guess_str.lower() == 'm':
        move_mode = not move_mode
        if move_mode:
            print("Move Mode is now on.")
        else:
            print("Move Mode is now off.")
        continue
    try:
        guess = int(guess_str)
        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break
        elif guess < secret_number:
            print("Your guess is smaller than the secret number. Try again.")
        else:
            print("Your guess is bigger than the secret number. Try again.")

        if move_mode:
            change = random.randint(-2, 2)
            secret_number += change
            if secret_number > 20:
                secret_number = 20
            elif secret_number < 1:
                secret_number = 1
