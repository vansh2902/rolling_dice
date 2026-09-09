import random

def roll_dice():
    return random.randint(1,6)

while True:
    input("Please enter to roll the dice...")
    print(f"you rolled a {roll_dice()}")
    play_again = input("Roll again (Y/N): ").lower()
    if play_again != "y":
        break


