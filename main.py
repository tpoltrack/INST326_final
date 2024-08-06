# main.py

from classes.character import Character
from classes.resource import Resource
from classes.event import Event
from classes.game import Game

def main():
    """
    Main function to start the game.
    """
    # Example of creating a character and starting the game
    player = Character(name="Trevor", role="Archer", skills={"archery": 5, "survival": 3})
    resources = Resource(food=10, ammo=5, medicines=3)
    game = Game()

    game.character = player
    game.resources = resources

    print("Game Started!")
    print(player)
    print(resources)

    # Add more game logic here

if __name__ == "__main__":
    main()