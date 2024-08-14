# classes/game.py

from .event import SnakeBiteEvent, ChestOfFoodEvent, AmmoBoxEvent, WeaselEvent, TravelerEvent
import json
from .character import Character
from .resource import Resource
import random

class Game:
    def __init__(self):
        """
        Initializes a new game instance.
        """
        self.character = None
        self.resources = None
        self.events = [AmmoBoxEvent(), WeaselEvent(), TravelerEvent(), SnakeBiteEvent(), ChestOfFoodEvent()]
        self.game_state = {}
        self.event_count = 0
        self.roles = {
            '1': 'Sharpshooter',
            '2': 'Explorer',
            '3': 'Pacifist'
        }

    def save_state(self):
        """
        Saves the current game state to a JSON file.
        """
        game_data = {
            'character': {
                'name': self.character.name if self.character else "",
                'role': self.character.role if self.character else "",
                'resources': {
                    'food': self.character.resources.food if self.character else 0,
                    'ammo': self.character.resources.ammo if self.character else 0,
                    'health': self.character.resources.health if self.character else 0,
                },
                'abilities': self.character.abilities if self.character else {'first': False, 'second': False, 'third': False},
                'unlocked_abilities': self.character.unlocked_abilities if self.character else []
            },
            'events': [str(event) for event in self.events],
            'game_state': self.game_state
        }

        with open('game_data.json', 'w') as file:
            json.dump(game_data, file, indent=4)
            print("\nGame Saved Successfully")

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
                resources=Resource(
                    food=game_data['character']['resources']['food'],
                    ammo=game_data['character']['resources']['ammo'],
                    health=game_data['character']['resources']['health']
                ),
                abilities=game_data['character'].get('abilities', {'first': False, 'second': False, 'third': False}),
                unlocked_abilities=game_data['character'].get('unlocked_abilities', [])
            )

            self.events = [SnakeBiteEvent(), ChestOfFoodEvent(), AmmoBoxEvent(), WeaselEvent(), TravelerEvent()]

            self.game_state = game_data['game_state']

            print("Game loaded successfully!")

        except FileNotFoundError:
            print("No saved game found.")
        except json.JSONDecodeError:
            print("Error reading the game data.")

    def start_game(self):
        """
        Starts the game by providing an introduction and initializing the character, resources, and events.
        """
        print("\nWelcome to Red Trail Frontier!")
        print("Prepare to embark on a perilous journey across the Wild West.")
        print("Face dangerous challenges, discover hidden treasures, and forge your destiny.")
        input("Press Enter to continue...")
        
        while True:
            choice = input("\nWould you like to (1) start a new game or (2) load a saved game? Enter 1 or 2: ").strip()
        
            if choice == '1':
                self._create_character()
                break
            elif choice == '2':
                self.load_state()
                if self.character is None:
                    print("No saved game found. Starting a new game instead.")
                    self._create_character()
                else:
                    print("Loaded saved game successfully!")
                    break
            else:
                print("Invalid choice. Please enter 1 or 2.")
                
        print("\nGame Has Started")

    def _create_character(self):
        """
        Handles character creation process.
        """
        if self.character is None or self.resources is None:
            print("\nLet's create your character.")
            name = input("Enter your character's name: ")
            role, abilities = self._choose_role()  # Ensure abilities is a dictionary

            resources = Resource(food=10, ammo=10, health=10)  # Initialize resources here
            self.character = Character(name=name, role=role, resources=resources, abilities=abilities)

            print("\nCharacter created successfully!")
            print(f"{'='*30}")
            print(self.character)
            print(f"{'='*30}")



    def _choose_role(self):
        """
        Prompts the user to choose a character role and displays available roles with predefined abilities and unlock requirements.

        :return: The chosen role as a string and its corresponding abilities.
        """
        # Defines abilities and their unlock requirements
        role_abilities = {
            'Sharpshooter': {
                'first': 'Increase success rate by 10% in shooting events.',
                'second': 'Increase success rate by 20% in shooting events.',
                'third': 'Increase success rate by 30% in shooting events.'
            },
            'Explorer': {
                'first': 'Chance to get +1 food or ammo on top of what is found.',
                'second': '10% increased chance of finding food or ammo in events.',
                'third': 'Losing one food will also restore one health.'
            },
            'Pacifist': {
                'first': '20% chance to flee from events that might take health away.',
                'second': '30% chance to flee from a hostile traveler.',
                'third': '30% chance to flee from events that might take health away.'
            }
        }

        print("\nChoose your role:")
        for key, role in self.roles.items():
            abilities = role_abilities[role]
            print(f"\n{key}. {role}")
            print("   Abilities:")
            for ability, description in abilities.items():
                print(f"     - {description} (Unlocks after {self._get_unlock_threshold(role, ability)} events)")

        choice = input("\nEnter the number of your chosen role: ")

        role_name = self.roles.get(choice, 'Unknown')
        abilities = role_abilities.get(role_name, {'first': False, 'second': False, 'third': False})
        
        return role_name, abilities

    def _get_unlock_threshold(self, role, ability):
        """
        Retrieves the unlock threshold for a given role and ability.

        :param role: The chosen character role.
        :param ability: The ability to check.
        :return: The number of events required to unlock the ability.
        """
        thresholds = {
            'Sharpshooter': {'first': 1, 'second': 10, 'third': 20},
            'Explorer': {'first': 1, 'second': 10, 'third': 20},
            'Pacifist': {'first': 1, 'second': 10, 'third': 20}
        }
        return thresholds.get(role, {}).get(ability, 'Unknown')

    def _get_role_abilities(self, role_name):
        """
        Retrieves the abilities for a given role.

        :param role_name: The name of the chosen role.
        :return: The abilities associated with the role.
        """
        # Placeholder for actual ability retrieval logic
        abilities = {
            'Sharpshooter': ['Increase success rate in shooting events'],
            'Explorer': ['Chance to get extra food or ammo'],
            'Pacifist': ['Chance to flee from health-threatening events']
        }
        return abilities.get(role_name, {'first': False, 'second': False, 'third': False})

    def show_character(self):
        """
        Displays the character information along with role-specific abilities.
        """
        if self.character:
            print("\nCharacter Information")
            print(f"{'='*30}")
            print(f"Name      : {self.character.name}")
            print(f"Role      : {self.character.role}")

            # Display abilities with descriptions
            abilities = self.character.abilities
            role = self.character.role

            if role == "Sharpshooter":
                descriptions = [
                    "10% increase in successfully shooting and killing any of the events that try to fight.",
                    "20% increase in success rate.",
                    "30% increase in success rate."
                ]
            elif role == "Explorer":
                descriptions = [
                    "Chance to get +1 food and ammo on top of what is found in events.",
                    "10% increased chance of finding food or ammo in events.",
                    "Losing one food will also restore one health."
                ]
            elif role == "Pacifist":
                descriptions = [
                    "20% chance to flee any event that might take health away.",
                    "30% chance to miss and flee from a hostile traveler.",
                    "30% chance to flee any event that might take health away."
                ]
            else:
                descriptions = ["???", "???", "???"]

            for i, (key, unlocked) in enumerate(abilities.items(), start=1):
                desc = descriptions[i-1] if unlocked else "???"
                print(f"Ability {i} : {desc}")

            print(f"{'='*30}")
        else:
            print("\nNo character created yet.")
    
    def show_resources(self):
        """
        Displays the current state of the character's resources.
        """
        if self.character:
            print("\nCharacter Resources:")
            print("==============================")
            print(f"Food      : {self.character.resources.food}")
            print(f"Ammo      : {self.character.resources.ammo}")
            print(f"Health    : {self.character.resources.health}")
            print("==============================")
        else:
            print("No character has been created yet.")
            
    
    def game_over(self):
        """
        Handles the game over scenario when the character's food or health reaches 0.
        """
        
        print("\nGame Over!")
        print("Your character has run out of food or health.")
        self.show_character()
        self.show_resources()

        restart = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if restart == 'yes':
            self.__init__()  # Reinitialize the game
            self.start_game()
        else:
            print("Thank you for playing! Goodbye!")
            exit()
            
    def end_game(self):
        """
        Handles the end of the game scenario when the player reaches round 30.
        """
        print("\nCongratulations! You've reached your destination and are soon to be called home.")
        print("You have successfully completed your journey.")
        print(f"\nSummary:")
        print(f"Name      : {self.character.name}")
        print(f"Role      : {self.character.role}")
        print(f"Food      : {self.character.resources.food}")
        print(f"Ammo      : {self.character.resources.ammo}")
        print(f"Health    : {self.character.resources.health}")
        print(f"Rounds Completed: {self.event_count}")
    
        # Exit the game
        print("Thank you for playing Red Trail Frontier!")
        exit()
        

    def apply_random_event(self):
        """
        Applies a random event to the character and updates the game state.
        """
        if self.character:
            # Check if the game is over before processing any event
            if self.character.resources.food <= 0 or self.character.resources.health <= 0:
                self.game_over()
                return

            # 33% chance to lose one food per round
            if random.random() < 0.33:
                self.character.resources.food = max(0, self.character.resources.food - 1)
                print("\nYou feel a bit hungry and lose 1 food.")
                
                # Check for game over immediately after reducing food
                if self.character.resources.food <= 0:
                    self.game_over()
                    return

            # Check again if the game is over before applying a new event
            if self.character.resources.food <= 0 or self.character.resources.health <= 0:
                self.game_over()
                return

            # Process an event if the game is not over
            if self.event_count >= 30:
                self.end_game()
                return
            
            event = random.choice(self.events)

            # Apply role-specific abilities
            success_rate = event.calculate_success_rate()
            success_rate = self.character.apply_role_ability(event.event_type, success_rate)

            # Process the event
            result = event.process_event(self.character, self.character.resources, success_rate)

            # Check for game over after processing the event
            if self.character.resources.food <= 0 or self.character.resources.health <= 0:
                self.game_over()
                return

            self.event_count += 1
            self.character.unlock_ability(self.event_count)
            
            # Show character and resources after the event
            self.show_character()
            self.show_resources()
        else:
            print("No character has been created yet.")
            
        
    def restart(self):
        """
        Restarts the game by resetting character and resources, and resetting the event count.
        """
        print("\nRestarting the game...")

        # Reset character and resources
        self.character = None
        self.resources = None
        self.event_count = 0

        print("\nThe game has been reset.")
        
        self.start_game()