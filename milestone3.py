import random

def high_low_game():
    # Welcome message
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    # Generate the computer's number (for example, between 1 and 100)
    computer_number = random.randint(1, 100)

    # Let's assume for this example, the user's number is manually set to 3
    user_number = 3

    # Show the computer's number for testing (in a real game, this would be hidden)
    print(f"The computer's number is {computer_number}")

    # User makes a guess
    user_guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()

    # Determine if the user's guess is correct
    if user_number < computer_number and user_guess == 'lower':
        print("You were right! The computer's number was higher.")
    elif user_number > computer_number and user_guess == 'higher':
        print("You were right! The computer's number was lower.")
    elif user_number == computer_number:
        print("The numbers are the same. The computer wins!")
    else:
        print(f"Sorry, you were wrong. The computer's number was {computer_number}.")

# Run the game
high_low_game()
