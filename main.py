#classes/main.py

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
        print(f"Name      : {character.name}")
        print(f"Role      : {character.role}")
        print(f"Abilities : {character.abilities}")
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
        print(f"Health     : {resources.health}")
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

        if choice == '1':
            game.show_character()
        elif choice == '2':
            game.show_resources()
        elif choice == '3':
            game.apply_random_event()
        elif choice == '4':
            game.save_state()
        elif choice == '5':
            game.restart()
        elif choice == '6':
            print("Thank you for playing Red Trail Redemption!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()