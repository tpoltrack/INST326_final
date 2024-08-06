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

def display_character(character):
    """
    Displays the character information in a formatted manner.
    """
    if character:
        print("\nCharacter Information")
        print(f"{'='*30}")
        print(f"Name     : {character.name}")
        print(f"Role     : {character.role}")
        print(f"Skills   : {character.skills}")
        print(f"{'='*30}")
    else:
        print("\nNo character created yet.")

def display_resources(resources):
    """
    Displays the resource status in a formatted manner.
    """
    if resources:
        print("\nResource Status")
        print(f"{'='*30}")
        print(f"Food       : {resources.food}")
        print(f"Ammo       : {resources.ammo}")
        print(f"Medicines  : {resources.medicines}")
        print(f"{'='*30}")
    else:
        print("\nNo resources initialized yet.")

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
            display_character(game.character)
        elif choice == "2":
            display_resources(game.resources)
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