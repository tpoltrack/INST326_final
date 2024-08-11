# classes/events.py

import random
from .resource import Resource

class Event:
    """
    Base class for defining an event in the game.
    """
    def __init__(self, description, effect):
        """
        Initializes an event with a description and effect.

        :param description: A string describing the event.
        :param effect: A dictionary where keys are resource names and values are changes to apply.
        """
        self.description = description
        self.effect = effect

    def __str__(self):
        """
        Returns a string representation of the event.

        :return: A string describing the event and its effect.
        """
        return f"{self.description} | Effect: {self.effect}"


class SnakeBiteEvent(Event):
    """
    Event where a snake tries to bite the player. If the player has ammo, they can use it to fight the snake.
    """
    def __init__(self):
        """
        Initializes the snake bite event with a description and effect.
        """
        description = "A snake tries to bite you! You can use ammo to fight it."
        effect = {}  # Effects will be applied in the handle_event method
        super().__init__(description, effect)

    def handle_event(self, resources):
        """
        Handles the snake bite event.

        :param resources: An instance of the Resource class to modify.
        :return: None
        """
        if resources.ammo > 0:
            # Player has ammo, chance to kill the snake
            resources.ammo -= 1
            if random.random() < 0.5:  # 50% chance to kill the snake
                print("You successfully killed the snake with your ammo. No health lost.")
            else:
                print("You missed the snake and it bites you. You lose 2 health.")
                resources.health = max(0, resources.health - 2)  # Deduct health, ensure it does not go below 0
        else:
            print("You have no ammo to fight the snake. It bites you, and you lose 2 health.")
            resources.health = max(0, resources.health - 2)  # Deduct health, ensure it does not go below 0
            
            
class ChestOfFoodEvent(Event):
    """
    Event where the player finds a chest of food. The chest contains between 1 to 3 units of food.
    """
    def __init__(self):
        """
        Initializes the chest of food event with a description and effect.
        """
        description = "You find a chest of food! It contains between 1 to 3 units of food."
        effect = {}  # Effects will be applied in the handle_event method
        super().__init__(description, effect)

    def handle_event(self, resources):
        """
        Handles the chest of food event.

        :param resources: An instance of the Resource class to modify.
        :return: None
        """
        food_found = random.randint(1, 3)  # Randomly determine the amount of food found
        resources.food += food_found
        print(f"You found {food_found} units of food in the chest.")
