# INST326_final
 Trevor Poltrack's INST326 Final Project 

# Red Trail Redemption

## Project Overview

"Red Trail Redemption" is a text-based adventure game where players make strategic decisions to navigate the Wild West American frontier. The game features character creation, resource management, and event handling, all implemented in Python.

## Features

- **Character Creation**: Create a character with a name, role, and skills.
- **Resource Management**: Manage inventory items like food, ammunition, and medical supplies.
- **Travel and Events**: Choose travel routes and respond to random events.
- **Challenges and Quests**: Engage in quests and face challenges.
- **Game End Conditions**: Conditions for completing the game or ending due to resource depletion.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/tpoltrack/INST326_final.git
    ```

2. Navigate to the project directory:

    ```bash
    cd INST326_final
    ```

## Usage

1. Run the main game script:

    ```bash
    python main.py
    ```

2. Follow the on-screen instructions to create a character, manage resources, and navigate the game.

## Directory Structure

INST326_final/
├── .gitattributes
├── .gitignore
├── README.md
├── main.py
├── game_data.json (to be created upon running the game)
└── classes/
├── init.py
├── character.py
├── resource.py
├── event.py
└── game.py

perl
Copy code

## Classes

- **Character**: Manages character attributes, skills, and inventory.
- **Resource**: Manages resources like food, ammo, and medicines.
- **Event**: Represents events that affect the game.
- **Game**: Manages the game state and interactions, including saving and loading game state.

## Game State Management

- **`game_data.json`**: File to store the game state.
- **`save_state()`**: Method in the `Game` class to save the current game state to `game_data.json`.
- **`load_state()`**: Method in the `Game` class to load the game state from `game_data.json`.

## Contributing

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature
    ```
3. Make your changes.
4. Commit your changes:
    ```bash
    git commit -am 'Add new feature'
    ```
5. Push to the branch:
    ```bash
    git push origin feature/your-feature
    ```
6. Create a new Pull Request.

## Acknowledgments

- Thanks to Matthew Patrick, Jong Ho Lee, and Goutham Patchipulusu for the guidance and support.
