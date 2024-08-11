# classes/character.py

class Character:
    def __init__(self, name, role, resources, abilities=None):
        """
        Initializes a character with a name, role, abilities, and resources.

        :param name: The name of the character.
        :param role: The role of the character.
        :param resources: An instance of the Resource class for the character.
        :param abilities: A dictionary of abilities for the character.
        """
        self.name = name
        self.role = role
        self.resources = resources  # Changed from inventory to resources
        self.abilities = {'first': False, 'second': False, 'third': False}

    def _initialize_abilities(self):
        abilities = {'first': False, 'second': False, 'third': False}
        return abilities

    def unlock_ability(self, event_count):
        """
        Unlocks abilities based on the number of events completed.

        :param event_count: The number of events completed.
        """
        if event_count >= 20:
            self.abilities['third'] = True
        if event_count >= 10:
            self.abilities['second'] = True
        if event_count >= 1:
            self.abilities['first'] = True

    def apply_role_ability(self, event_type, success_rate):
        if self.role == 'Sharpshooter':
            if self.abilities['third']:
                success_rate += 0.30
            elif self.abilities['second']:
                success_rate += 0.20
            elif self.abilities['first']:
                success_rate += 0.10
        elif self.role == 'Explorer':
            if self.abilities['third'] and event_type in ['food', 'ammo']:
                success_rate += 1
            elif self.abilities['second'] and event_type in ['food', 'ammo']:
                success_rate += 0.10
            elif self.abilities['first'] and event_type in ['food', 'ammo']:
                success_rate += 1
        elif self.role == 'Pacifist':
            if event_type == 'health':
                if self.abilities['third']:
                    success_rate += 0.30
                elif self.abilities['second']:
                    success_rate += 0.30
                elif self.abilities['first']:
                    success_rate += 0.20
        return success_rate

    def __str__(self):
        return f"Name: {self.name}, Role: {self.role}, Resources: {self.resources}, Abilities: {self.abilities}"
