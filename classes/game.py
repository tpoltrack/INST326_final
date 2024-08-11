# classes/game.py

from .event import SnakeBiteEvent, ChestOfFoodEvent, AmmoBoxEvent, WeaselEvent, TravelerEvent
import json
from .character import Character
from .resource import Resource
import random

class Game:
    """
    Manages the game state and interactions.

    Attributes:
        character (Character): The main character in the game.
        resources (Resource): The resources available to the character.
        events (list): List of events that can occur in the game.
        game_state (dict): Dictionary to store the game state.
    """

    def __init__(self):
        """
        Initializes a new game instance.
        """
        self.character = None
        self.resources = None
        self.events = []
        self.game_state = {}
        self.event_count = 0  # Counter for events applied

    def save_state(self):
        """
        Saves the current game state to a JSON file.
        """
        game_data = {
            'character': {
                'name': self.character.name if self.character else "",
                'role': self.character.role if self.character else "",
                'skills': self.character.skills if self.character else {},
                'inventory': self.character.inventory if self.character else {},
            },
            'resources': {
                'food': self.resources.food if self.resources else 0,
                'ammo': self.resources.ammo if self.resources else 0,
                'health': self.resources.health if self.resources else 0,
            },
            'events': [str(event) for event in self.events],
            'game_state': self.game_state
        }

        with open('game_data.json', 'w') as file:
            json.dump(game_data, file, indent=4)

    def load_state(self):
        """
        Loads the game state from a JSON file.
        """
        try:
            with open('game_data.json', 'r') as file:
                game_data = json.load(file)

            self.character = Character(
                name=game_data['character']['name'],
                role=game_data['character']['role'],
                skills=game_data['character']['skills'],
                inventory=game_data['character']['inventory']
            )

            self.resources = Resource(
                food=game_data['resources']['food'],
                ammo=game_data['resources']['ammo'],
                health=game_data['resources']['health']
            )

            self.events = [SnakeBiteEvent(), ChestOfFoodEvent(), AmmoBoxEvent(), WeaselEvent(), TravelerEvent()]

            self.game_state = game_data['game_state']
        except FileNotFoundError:
            print("No saved game found.")
        except json.JSONDecodeError:
            print("Error reading the game data.")

    def start_game(self):
        """
        Starts the game by providing an introduction and initializing the character, resources, and events.
        """
        # Welcome message
        print("\nWelcome to Red Trail Frontier!")
        print("Prepare to embark on a perilous journey across the Wild West.")
        print("Face dangerous challenges, discover hidden treasures, and forge your destiny.")
        input("Press Enter to continue...")

        # Prompt for character creation
        if self.character:
            print("\nLet's create your character.")
            name = input("Enter your character's name: ")
            role = self._choose_role()

            # Initialize character with role-based skills and default inventory
            skills = self._get_role_skills(role)
            inventory = {
                'food': 10,
                'ammo': 10,
                'health': 10
            }
            self.character = Character(name=name, role=role, skills=skills, inventory=inventory)

            print("\nCharacter created successfully!")
            print(f"{'='*30}")
            print(self.character)
            print(f"{'='*30}")

        # Initialize resources
        if not self.resources:
            print("\nInitializing default resources.")
            self.resources = Resource(food=10, ammo=10, health=10)

        # Initialize events
        if not self.events:
            self.events.append(SnakeBiteEvent())  # Ensure SnakeBiteEvent is initialized
            self.events.append(ChestOfFoodEvent())  # Add ChestOfFoodEvent

        print("\nGame Started!")

    def _choose_role(self):
        """
        Prompts the user to choose a character role and displays available roles with predefined skills.

        :return: The chosen role as a string.
        """
        roles = {
            'Melee': {'damage': 7, 'defense': 9, 'speed': 3, 'sneak': 2},
            'Archer': {'damage': 3, 'defense': 4, 'speed': 8, 'sneak': 6},
            'Mage': {'damage': 6, 'defense': 5, 'speed': 5, 'sneak': 6}
        }

        print("\nChoose your role:")
        for i, (role, skills) in enumerate(roles.items(), 1):
            print(f"{i}. {role}")
            print(f"   Skills: Damage={skills['damage']}, Defense={skills['defense']}, Speed={skills['speed']}, Sneak={skills['sneak']}")
            print()

        while True:
            try:
                choice = int(input("Enter the number of your chosen role: "))
                if 1 <= choice <= len(roles):
                    return list(roles.keys())[choice - 1]
                else:
                    print("Invalid choice. Please choose a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def _get_role_skills(self, role):
        """
        Retrieves the skill set based on the chosen role.

        :param role: The chosen character role.
        :return: A dictionary of skills for the chosen role.
        """
        role_skills = {
            'Melee': {'damage': 7, 'defense': 9, 'speed': 3, 'sneak': 2},
            'Archer': {'damage': 3, 'defense': 4, 'speed': 8, 'sneak': 6},
            'Mage': {'damage': 6, 'defense': 5, 'speed': 5, 'sneak': 6}
        }
        return role_skills.get(role, {'damage': 0, 'defense': 0, 'speed': 0, 'sneak': 0})

    def show_character(self):
        """
        Displays the character's details.

        :return: None
        """
        if self.character:
            print("\nCharacter Information:")
            print(f"{'='*30}")
            print(self.character)
            print(f"{'='*30}")
        else:
            print("No character created yet.")

    def show_resources(self):
        """
        Displays the current resources status.

        :return: None
        """
        if self.resources:
            print("\nResource Status:")
            print(f"{'='*30}")
            print(f"Food   : {self.resources.food}")
            print(f"Ammo   : {self.resources.ammo}")
            print(f"Health : {self.resources.health}")
            print(f"{'='*30}")
        else:
            print("Resources not initialized yet.")

    def initialize(self):
        """
        Initializes the game with default character, resources, and events.
        """
        self.character = Character("Default", "Explorer", {"damage": 5, "defense": 5, "speed": 5, "sneak": 5})
        self.resources = Resource(health=10, food=10, ammo=10)
        self.events = [SnakeBiteEvent(), ChestOfFoodEvent(), AmmoBoxEvent(), WeaselEvent(), TravelerEvent()]  # Initialize with SnakeBiteEvent

    def apply_random_event(self):
        """
        Applies a random event to the game, affecting resources based on event effects.
        """
        event = random.choice(self.events)
        print(f"\nEvent: {event.description}")
        event.handle_event(self.resources)
        self.show_resources()  # Show updated resources after event
        
        # Increment the event counter
        self.event_count += 1

        # Drop food level after every 3-5 events
        if self.event_count % random.randint(3, 5) == 0:
            self.resources.food = max(0, self.resources.food - 1)
            print(f"Food level has dropped by 1. Current food: {self.resources.food}")
        
        if self.check_game_over():
            self.restart_or_quit()

    def __str__(self):
        """
        Returns a string representation of the game.

        Returns:
            str: A string description of the game state.
        """
        return f"Character: {self.character}, Resources: {self.resources}, Events: {self.events}, Game State: {self.game_state}"

    def restart(self):
        """
        Restarts the game by re-initializing character, resources, and events.
        """
        self.initialize()
        print("Game has been restarted.")
        
    def check_game_over(self):
        """
        Checks if the game is over due to health or food reaching 0.
        """
        if self.resources.health <= 0:
            print("Game Over! You have died.")
            return True
        if self.resources.food <= 0:
            print("Game Over! You have starved to death.")
            return True
        return False
    
    def restart_or_quit(self):
        """
        Asks the player if they want to restart the game or quit.
        """
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice == 'yes':
            self.__init__()  # Reinitialize the game
            self.start_game()
        else:
            print("Thank you for playing Red Trail Redemption!")
            exit()  # Exit the program
