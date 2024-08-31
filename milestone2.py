import random

# Generate random numbers
computer_number = random.randint(1, 100)
your_number = random.randint(1, 100)

# Print the numbers
print("Welcome to the High-Low Game!")
print("--------------------------------")
print(f"The computer's number is {computer_number}")
print(f"Your number is {your_number}")

# Get the user's choice
user_choice = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").lower()

# Print the user's choice (for testing purposes)
print(f"You chose: {user_choice}")
