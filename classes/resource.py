# classes/resource.py

class Resource:
    """
    Manages resources in the game.

    Attributes:
        food (int): Amount of food.
        ammo (int): Amount of ammunition.
        health (int): Amount of health.
    """

    def __init__(self, food=10, ammo=10, health=10):
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
        return f"Food: {self.food}, Ammo: {self.ammo}, Health: {self.health}"
    
    def add_food(self, amount):
        """
        Adds food to the resources, ensuring it does not exceed the maximum cap.

        :param amount: The amount of food to add.
        """
        self.food += amount
        
    def add_ammo(self, amount):
        """
        Adds ammo to the resource, allowing ammo to exceed the previous cap.
        """
        self.ammo += amount
