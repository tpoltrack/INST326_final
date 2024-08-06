# classes/game.py

import json
from .character import Character
from .resource import Resource
from .event import Event

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
            'events': [str(event) for event in self.events],  # Adjust if Event objects are complex
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
                skills=game_data['character']['skills']
            )
            self.character.inventory = game_data['character']['inventory']

            self.resources = Resource(
                food=game_data['resources']['food'],
                ammo=game_data['resources']['ammo'],
                health=game_data['resources']['health']
            )

            
            self.events = [Event(description=event, effect={}) for event in game_data['events']]
            
            self.game_state = game_data['game_state']
        except FileNotFoundError:
            print("No saved game found.")
        except json.JSONDecodeError:
            print("Error reading the game data.")

    def start_game(self):
        """
        Starts the game by providing an introduction and initializing the character, resources, and events.

        Prompts the player to create a character, sets initial inventory levels to 10, and initializes default resources and events.
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
            self.events.append(Event(description="A wild animal appears!", effect={'food': -2}))
            self.events.append(Event(description="You find a hidden stash of ammo!", effect={'ammo': 3}))

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

    def apply_event(self, event):
        """
        Applies an event to the current game state.

        Args:
            event (Event): The event to apply.
        """
        event.trigger(self.character)
        print(f"Event Applied: {event.description}")
        
    def restart_game(self):
        """
        Resets the game state to start from the beginning.
        """
        self.character = None
        self.resources = None
        self.events = []
        self.game_state = {}

        print("Game has been restarted.")
        self.start_game()  # Re-initialize the game

    def __str__(self):
        """
        Returns a string representation of the game.

        Returns:
            str: A string description of the game state.
        """
        return f"Character: {self.character}, Resources: {self.resources}, Events: {self.events}, Game State: {self.game_state}"