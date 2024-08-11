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
        

class AmmoBoxEvent(Event):
    """
    Event where the player finds an ammo box. The box contains either 2 or 3 ammo.
    """
    def __init__(self):
        """
        Initializes the ammo box event with a description and effect.
        """
        description = "You find an ammo box! It contains either 2 or 3 ammo."
        effect = {}  # Effects will be applied in the handle_event method
        super().__init__(description, effect)

    def handle_event(self, resources):
        """
        Handles the ammo box event.

        :param resources: An instance of the Resource class to modify.
        :return: None
        """
        ammo_found = random.choice([2, 3])  # Randomly determine the amount of ammo found
        resources.ammo = min(resources.ammo + ammo_found, 100)  # Cap ammo at 100
        print(f"You found {ammo_found} ammo in the box.")


class WeaselEvent(Event):
    """
    Event where the player encounters a weasel trying to steal food.
    """
    def __init__(self):
        """
        Initializes the weasel event with a description and effect.
        """
        description = "A weasel tries to steal your food! You can try to kill it with ammo."
        effect = {}  # Effects will be applied in the handle_event method
        super().__init__(description, effect)

    def handle_event(self, resources):
        """
        Handles the weasel event.

        :param resources: An instance of the Resource class to modify.
        :return: None
        """
        if resources.ammo > 0:
            # Player has ammo, chance to kill the weasel
            resources.ammo -= 1
            if random.random() < 0.5:  # 50% chance to kill the weasel
                print("You successfully killed the weasel with your ammo. It didn't steal any food.")
            else:
                food_stolen = random.randint(1, 3)  # Randomly determine the amount of food stolen
                resources.food = max(0, resources.food - food_stolen)  # Deduct stolen food, ensure it does not go below 0
                print(f"The weasel escaped and stole {food_stolen} units of food.")
        else:
            food_stolen = random.randint(1, 3)  # Randomly determine the amount of food stolen
            resources.food = max(0, resources.food - food_stolen)  # Deduct stolen food, ensure it does not go below 0
            print(f"The weasel steals {food_stolen} units of food from you.")


class TravelerEvent(Event):
    """
    Event where the player encounters a traveler who could be good or bad.
    """
    def __init__(self):
        """
        Initializes the traveler event with a description and effect.
        """
        description = "You encounter a traveler who could be friendly or hostile."
        effect = {}  # Effects will be applied in the handle_event method
        super().__init__(description, effect)

    def handle_event(self, resources):
        """
        Handles the traveler event.

        :param resources: An instance of the Resource class to modify.
        :return: None
        """
        if random.random() < 0.5:  # 50% chance traveler is good
            print("The traveler is friendly and offers you a place to rest. Your health is restored to 10.")
            resources.health = 10
        else:  # Traveler is hostile
            print("The traveler is hostile! You need to fight him.")
            while True:
                if resources.ammo > 0:
                    action = input("Do you want to use ammo to fight the traveler? (yes/no): ").strip().lower()
                    if action == 'yes':
                        resources.ammo -= 1
                        if random.random() < 0.5:  # 50% chance the traveler will shoot
                            resources.health = max(0, resources.health - 3)  # Deduct health, ensure it does not go below 0
                            print("You killed the traveler, but he shot you and you lost 3 health.")
                        else:
                            print("You killed the traveler and avoided being shot.")
                        break
                    else:
                        print("You missed the chance to fight. The traveler continues to attack!")
                else:
                    print("You have no ammo to fight the traveler. The traveler steals 3 health from you.")
                    resources.health = max(0, resources.health - 3)  # Deduct health, ensure it does not go below 0
                    break