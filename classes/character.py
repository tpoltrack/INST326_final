# classes/character.py

class Character:
    def __init__(self, name, role, skills, inventory=None):
        """
        Initializes a new character with the given name, role, skills, and inventory.

        :param name: Character's name.
        :param role: Character's role (e.g., Melee, Archer, Mage).
        :param skills: Dictionary of skills (damage, defense, speed, sneak).
        :param inventory: Dictionary of inventory items (food, ammo, health). Defaults to {'food': 0, 'ammo': 0, 'health': 0}.
        """
        self.name = name
        self.role = role
        self.skills = skills  # Dictionary with keys: 'damage', 'defense', 'speed', 'sneak'
        self.inventory = inventory if inventory else {'food': 10, 'ammo': 10, 'health': 10}

    def __str__(self):
        """
        Returns a string representation of the character, including skills and inventory.

        :return: A formatted string of the character's name, role, skills, and inventory.
        """
        skills_str = (f"Damage={self.skills.get('damage', 0)}, "
                      f"Defense={self.skills.get('defense', 0)}, "
                      f"Speed={self.skills.get('speed', 0)}, "
                      f"Sneak={self.skills.get('sneak', 0)}")
        inventory_str = (f"Food={self.inventory.get('food', 0)}, "
                         f"Ammo={self.inventory.get('ammo', 0)}, "
                         f"Health={self.inventory.get('health', 0)}")
        return (f"Name     : {self.name}\n"
                f"Role     : {self.role}\n"
                f"Skills   : {skills_str}\n"
                f"Inventory: {inventory_str}")
