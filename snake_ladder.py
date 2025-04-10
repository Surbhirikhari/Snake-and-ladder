import random

# Snakes and ladders positions
SNAKES = {17: 7, 54: 34, 62: 19, 98: 79}
LADDERS = {3: 22, 8: 26, 20: 38, 28: 84, 71: 91}

# Starting position at 0
position = 0

def print_board():
    """Simple function to print the current status."""
    print(f"Your current position: {position}")

print("Welcome to Snake & Ladder!")
name = input("Enter your name: ")

while position < 100:
    # Provide instructions to roll the dice
    print_board()
    input("Press Enter to roll the dice...")
    dice = random.randint(1, 6)
    print(f"You rolled: {dice}")

    # Move player by the dice number
    position += dice

    # Check if the player landed on a snake
    if position in SNAKES:
        print(f"Oh no! A snake! You fell from {position} to {SNAKES[position]}")
        position = SNAKES[position]

    # Check if the player landed on a ladder
    elif position in LADDERS:
        print(f"Yay! A ladder! You climbed from {position} to {LADDERS[position]}")
        position = LADDERS[position]

    # If the position exceeds 100, the player cannot move further
    if position > 100:
        position -= dice  # Ignore move if it goes over 100
        print("You need an exact roll to win! Try again.")

    # Display the player's new position
    print(f"Your new position: {position}\n")

    # Check for game completion
    if position == 100:
        print(f"Congratulations {name}, you won!")
        break

