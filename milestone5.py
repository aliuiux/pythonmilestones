import random

def high_low_game():
    # Constants
    NUM_ROUNDS = 3
    
    # Initialize player score
    player_score = 0

    # Welcome message
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        # Generate the computer's number (for example, between 1 and 100)
        computer_number = random.randint(1, 100)

        # Let's assume for this example, the user's number is randomly generated as well
        user_number = random.randint(1, 100)

        # Show the user's number
        print(f"Your number is {user_number}")

        # Safeguard user input
        while True:
            user_guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
            if user_guess in ['higher', 'lower']:
                break
            else:
                print("Invalid input! Please enter 'higher' or 'lower'.")

        # Determine if the user's guess is correct
        if user_number < computer_number and user_guess == 'lower':
            print(f"You were right! The computer's number was {computer_number}")
            player_score += 1
        elif user_number > computer_number and user_guess == 'higher':
            print(f"You were right! The computer's number was {computer_number}")
            player_score += 1
        elif user_number == computer_number:
            print(f"The numbers are the same. The computer wins with {computer_number}!")
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        # Print the player's score after each round
        print(f"Your current score is: {player_score}")
        
        # Add a blank line to separate the rounds visually
        print()

    # Final score
    print(f"Game Over! Your final score is: {player_score}")

# Run the game
high_low_game()
