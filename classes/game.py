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
                'medicines': self.resources.medicines if self.resources else 0,
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
                medicines=game_data['resources']['medicines']
            )

            # If Event class is complex, you may need to parse it differently
            self.events = [Event(description=event, effect={}) for event in game_data['events']]
            
            self.game_state = game_data['game_state']
        except FileNotFoundError:
            print("No saved game found.")
        except json.JSONDecodeError:
            print("Error reading the game data.")

    def start_game(self):
        """
        Starts the game by initializing the character, resources, and events.
        """
        # Example initialization; adjust as needed
        if not self.character:
            print("Creating default character.")
            self.character = Character(name="Default", role="Explorer", skills={"exploration": 5})
        if not self.resources:
            print("Initializing default resources.")
            self.resources = Resource(food=10, ammo=5, medicines=3)
        
        # Example of adding random events
        self.events.append(Event(description="A wild animal appears!", effect={'food': -2}))
        self.events.append(Event(description="You find a hidden stash of ammo!", effect={'ammo': 3}))

        print("Game Initialized!")
        print(self.character)
        print(self.resources)

    def apply_event(self, event):
        """
        Applies an event to the current game state.

        Args:
            event (Event): The event to apply.
        """
        event.trigger(self.character)
        print(f"Event Applied: {event.description}")

    def __str__(self):
        """
        Returns a string representation of the game.

        Returns:
            str: A string description of the game state.
        """
        return f"Character: {self.character}, Resources: {self.resources}, Events: {self.events}, Game State: {self.game_state}"