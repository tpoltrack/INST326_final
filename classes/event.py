# classes/event.py

import random

class Event:
    """
    Represents an event that can affect the game.

    Attributes:
        description (str): Description of the event.
        effect (dict): Dictionary of effects on character's resources.
    """

    def __init__(self, description, effect):
        """
        Initializes an event with a description and effect.

        Args:
            description (str): Description of the event.
            effect (dict): Effect of the event on resources.
        """
        self.description = description
        self.effect = effect

    def trigger(self, character):
        """
        Applies the event's effect to the given character.

        Args:
            character (Character): The character affected by the event.
        """
        # Example of applying the effect (details depend on your implementation)
        for resource, change in self.effect.items():
            if resource in character.inventory:
                character.inventory[resource] += change

    def __str__(self):
        """
        Returns a string representation of the event.

        Returns:
            str: A string description of the event.
        """
        return f"Event: {self.description}, Effect: {self.effect}"
    

