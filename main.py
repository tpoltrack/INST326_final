# main.py

from classes.game import Game

def main():
    """
    Main function to start and run the game.
    """
    game = Game()
    
    # Optionally, load a previously saved game state
    game.load_state()

    # Start the game
    game.start_game()

    # Main game loop
    while True:
        print("\nMenu:")
        print("1. Show Character")
        print("2. Show Resources")
        print("3. Apply Random Event")
        print("4. Save Game")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(game.character)
        elif choice == "2":
            print(game.resources)
        elif choice == "3":
            if game.events:
                import random
                event = random.choice(game.events)
                game.apply_event(event)
            else:
                print("No events available.")
        elif choice == "4":
            game.save_state()
            print("Game saved.")
        elif choice == "5":
            game.save_state()  # Save game state before exiting
            print("Exiting game.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
