# main.py

from classes.game import Game

def display_menu():
    """
    Displays the main menu to the player.
    """
    print("\n=== Red Trail Redemption ===")
    print("1. Show Character")
    print("2. Show Resources")
    print("3. Apply Random Event")
    print("4. Save Game")
    print("5. Restart Game")
    print("6. Exit")
    print("============================")

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
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            print("\n=== Character Info ===")
            print(game.character)
            print("======================")
        elif choice == "2":
            print("\n=== Resource Info ===")
            print(game.resources)
            print("=====================")
        elif choice == "3":
            if game.events:
                import random
                event = random.choice(game.events)
                game.apply_event(event)
                print(f"\nEvent Applied: {event.description}")
            else:
                print("\nNo events available.")
        elif choice == "4":
            game.save_state()
            print("\nGame saved successfully.")
        elif choice == "5":
            game.restart_game()
        elif choice == "6":
            game.save_state()  # Save game state before exiting
            print("\nExiting game. Goodbye!")
            break
        else:
            print("\nInvalid option, please try again.")

if __name__ == "__main__":
    main()