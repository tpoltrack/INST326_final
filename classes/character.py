# classes/character.py

class Character:
    """
    Represents a character in the game.

    Attributes:
        name (str): The name of the character.
        role (str): The role of the character (e.g., archer, melee).
        skills (dict): Dictionary of skills and their levels.
        inventory (dict): Dictionary of inventory items (food, ammo, medicines).
    """

    def __init__(self, name, role, skills):
        """
        Initializes a new character with the given attributes.

        Args:
            name (str): The name of the character.
            role (str): The role of the character.
            skills (dict): The skills of the character.
        """
        self.name = name
        self.role = role
        self.skills = skills
        self.inventory = {'food': 0, 'ammo': 0, 'medicines': 0}

    def __str__(self):
        """
        Returns a string representation of the character.

        Returns:
            str: A string description of the character.
        """
        return f"Name: {self.name}, Role: {self.role}, Skills: {self.skills}, Inventory: {self.inventory}"
    
