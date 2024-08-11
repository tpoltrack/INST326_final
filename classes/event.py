#classes/event.py

import random

class Event:
    """
    Base class for events in the game.
    """
    def __init__(self, event_type):
        """
        Initializes an event with a specific event type.
        """
        self.event_type = event_type

    def process_event(self, character, resources, success_rate):
        """
        Processes the event. This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def calculate_success_rate(self):
        """
        Calculates the success rate of the event.
        """
        return random.random()


class AmmoBoxEvent(Event):
    """
    Represents an ammo box event that gives the player extra ammo.
    """
    def __init__(self):
        super().__init__('ammo_box')
    
    def process_event(self, character, resources, success_rate):
        """
        Processes the ammo box event.
        """
        # Determine the amount of ammo found (2 or 3 pieces)
        ammo_found = random.randint(2, 3)
        
        # Add the found ammo to the character's resources
        resources.add_ammo(ammo_found)
        
        print(f"You found an ammo box! Gained {ammo_found} ammo.")
        return True


class WeaselEvent(Event):
    """
    Represents a weasel event that tries to steal food.
    """
    def __init__(self):
        super().__init__('weasel')
    
    def process_event(self, character, resources, success_rate):
        """
        Processes the weasel event.
        """
        # Set a default success rate of 50%
        default_success_rate = 0.5
        
        # Use the provided success rate if it's greater than the default
        effective_success_rate = max(success_rate, default_success_rate)

        if random.random() < effective_success_rate:
            food_stolen = random.randint(1, 3)
            resources.food -= food_stolen
            if resources.food < 0:
                resources.food = 0
            print(f"The weasel stole {food_stolen} food!")
            return False
        else:
            ammo_used = 1
            resources.ammo -= ammo_used
            if resources.ammo < 0:
                resources.ammo = 0
            print(f"You managed to scare off the weasel using 1 ammo!")
            return True

import random

class TravelerEvent(Event):
    """
    Represents a traveler event with various outcomes based on player choices.
    """
    def __init__(self):
        super().__init__('traveler')
    
    def process_event(self, character, resources, success_rate):
        """
        Processes the traveler event.
        """
        # Prompt the player to shoot or not
        shoot_choice = input("Do you want to shoot the traveler? (yes/no): ").strip().lower()
        
        if shoot_choice == 'yes':
            # 50/50 chance to kill the traveler
            if random.random() < 0.5:
                print("You successfully shot the traveler!")
                resources.health = 10
                return True
            else:
                print("You missed the shot. The traveler retaliates!")
                if random.random() < 0.5:
                    print("The traveler hits you. You lose 4 health.")
                    resources.health -= 4
                else:
                    print("The traveler misses you. You lose 3 food.")
                    resources.food = max(0, resources.food - 3)
                return True
        else:
            # 50/50 chance the traveler is good or bad
            if random.random() < 0.5:
                print("The traveler is good and lets you stay at his camp. Your health is restored to 10.")
                resources.health = 10
            else:
                print("The traveler is bad. He tries to shoot you!")
                if random.random() < 0.5:
                    print("The traveler hits you. You lose 4 health.")
                    resources.health -= 4
                else:
                    print("The traveler misses you. You lose 3 food.")
                    resources.food = max(0, resources.food - 3)
                
                # 50/50 chance to hit the traveler
                if random.random() < 0.5:
                    print("You manage to hit the traveler. You take some of his supplies.")
                    if random.random() < 0.5:
                        ammo_found = random.randint(1, 3)
                        resources.add_ammo(ammo_found)
                        print(f"Gained {ammo_found} ammo.")
                    else:
                        food_found = random.randint(1, 3)
                        resources.add_food(food_found)
                        print(f"Gained {food_found} food.")
                else:
                    print("You miss the traveler. No extra supplies gained.")
            return True

class SnakeBiteEvent(Event):
    """
    Represents a snake bite event that affects health.
    """
    def __init__(self):
        super().__init__('snake_bite')
    
    def process_event(self, character, resources, success_rate):
        """
        Processes the snake bite event.
        """
        # Set a default success rate of 50%
        default_success_rate = 0.5
        
        # Use the provided success rate if it's greater than the default
        effective_success_rate = max(success_rate, default_success_rate)

        if random.random() < effective_success_rate:
            print("You managed to kill the snake!")
            return True
        else:
            # If the snake is not killed, it will bite the character
            health_lost = random.randint(1, 3)
            resources.health -= health_lost
            if resources.health < 0:
                resources.health = 0
            print(f"The snake bit you! Lost {health_lost} health.")
            return False

import random

class ChestOfFoodEvent(Event):
    """
    Represents a chest of food event that gives the player extra food.
    """
    def __init__(self):
        super().__init__('chest_of_food')
    
    def process_event(self, character, resources, success_rate):
        """
        Processes the chest of food event.
        """
        # Determine the amount of food found (1 or 2 pieces)
        food_found = random.randint(1, 2)
        
        # Add the found food to the character's resources
        resources.add_food(food_found)
        
        print(f"You found a chest of food! Gained {food_found} food.")
        return True
