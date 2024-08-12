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
    Represents a weasel encounter event with options to flee or fight.
    """
    def __init__(self):
        super().__init__('weasel')

    def process_event(self, character, resources, success_rate):
        """
        Processes the weasel encounter event with options to flee or fight.
        """
        print("You have encountered a weasel!")

        while True:
            flee_choice = input("Do you wish to try to flee? (y/n): ").strip().lower()
            
            if flee_choice == 'y':
                # 50/50 chance to flee successfully
                if random.random() < 0.5:
                    print("You successfully fled from the weasel!")
                    return True
                else:
                    stolen_food = random.randint(1, 3)
                    print(f"You failed to flee. The weasel stole {stolen_food} food!")
                    resources.food -= stolen_food
                    return True
            elif flee_choice == 'n':
                # Player chooses to fight the weasel
                print("You chose to fight the weasel!")
                if random.random() < 0.5:
                    print("You managed to kill the weasel!")
                    resources.ammo -= 1
                    resources.food += 1
                    print("You lose 1 ammo.")
                else:
                    stolen_food = random.randint(1, 3)
                    print(f"You missed the weasel! It stole {stolen_food} food.")
                    resources.ammo -= 1
                    resources.food -= stolen_food
                    print("You lose 1 ammo and food.")
                return True
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


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
        while True:
            print("\nYou find a traveler and you are unsure of his intentions")
            shoot_choice = input("Do you want to shoot the traveler? (y/n): ").strip().lower()

            if shoot_choice == 'y':
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
            
            elif shoot_choice == 'n':
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
            
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

class SnakeBiteEvent(Event):
    """
    Represents a snake bite event with options to flee or fight.
    """
    def __init__(self):
        super().__init__('snakebite')

    def process_event(self, character, resources, success_rate):
        """
        Processes the snake bite event with options to flee or fight.
        """
        print("You have encountered a snake!")

        while True:
            flee_choice = input("Do you wish to try to flee? (y/n): ").strip().lower()
            
            if flee_choice == 'y':
                # 50/50 chance to flee successfully
                if random.random() < 0.5:
                    print("You successfully fled from the snake!")
                    return True
                else:
                    print("You failed to flee. The snake bites you!")
                    resources.health -= 2
                    print("You lose 2 health.")
                    return True
            elif flee_choice == 'n':
                # Player chooses to fight the snake
                print("You chose to fight the snake!")
                if random.random() < 0.5:
                    print("You managed to kill the snake!")
                    resources.ammo -= 1
                    resources.food += 1
                    print("You lose 1 ammo.")
                else:
                    print("You missed the snake!")
                    resources.ammo -= 1
                    resources.health -= 2
                    print("You lose 1 ammo and 2 health.")
                return True
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


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
