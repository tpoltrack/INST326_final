# classes/resource.py

class Resource:
    """
    Manages resources in the game.

    Attributes:
        food (int): Amount of food.
        ammo (int): Amount of ammunition.
        medicines (int): Amount of medical supplies.
    """

    def __init__(self, food=0, ammo=0, medicines=0):
        """
        Initializes resources with given amounts.

        Args:
            food (int): Amount of food.
            ammo (int): Amount of ammunition.
            medicines (int): Amount of medical supplies.
        """
        self.food = food
        self.ammo = ammo
        self.medicines = medicines

    def __str__(self):
        """
        Returns a string representation of the resources.

        Returns:
            str: A string description of the resources.
        """
        return f"Food: {self.food}, Ammo: {self.ammo}, Medicines: {self.medicines}"