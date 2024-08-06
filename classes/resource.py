# classes/resource.py

class Resource:
    """
    Manages resources in the game.

    Attributes:
        food (int): Amount of food.
        ammo (int): Amount of ammunition.
        health (int): Amount of health.
    """

    def __init__(self, food=0, ammo=0, health=0):
        """
        Initializes resources with given amounts.

        Args:
            food (int): Amount of food.
            ammo (int): Amount of ammunition.
            health (int): Amount of health.
        """
        self.food = food
        self.ammo = ammo
        self.health = health
    def __str__(self):
        """
        Returns a string representation of the resources.

        Returns:
            str: A string description of the resources.
        """
        return f"Food: {self.food}, Ammo: {self.ammo}, health: {self.health}"