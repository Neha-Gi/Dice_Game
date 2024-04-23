import time
from Dice_board import Game

def main():
    print("**Welcome to the Dice Game**\n")
    time.sleep(2)
    print("Here is an overview of the game...\n")
    print("You will use an 8-faced dice, and if anyone rolls a 4 or 8, their score will be reset to 0.")
    print("The winner is the first player to earn 50 points.")
    print("\nReady to start?")
    start_or_quit = input("Press Y or Q: ").lower()
    
    if start_or_quit == "y":
        num_players = int(input("Enter the number of players: "))
        game = Game(num_players)
        
        while True:  
            game.play_turn()

    elif start_or_quit == "q":
        print("Quitting the game...")

    else:
        print("Invalid input. Please enter 'Y' to start or 'Q' to quit.")


if __name__ == "__main__":
    main()