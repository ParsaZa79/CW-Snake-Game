# Snake Game

This is a classic Snake Game implemented using Python and the Pygame library. The objective of the game is to control a snake, move it around the game window, eat food to grow longer, and avoid colliding with the boundaries or the snake's own body.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Features](#game-features)
- [Code Structure](#code-structure)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

These instructions will help you get the game up and running on your local machine.

### Prerequisites

- Python 3.x
- Pygame library

### Installation

1. Clone the repository: https://github.com/ParsaZa79/CW-Snake-Game.git

2. Navigate to the project directory:
```bash
cd snake-game
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Run the game:
```bash
python snake_game.py
```

## How to Play

- Use the arrow keys to control the snake's movement:
- Up Arrow: Move the snake upwards
- Down Arrow: Move the snake downwards
- Left Arrow: Move the snake to the left
- Right Arrow: Move the snake to the right
- Eat the food (red squares) to grow longer and increase your score.
- Avoid colliding with the boundaries of the game window or the snake's own body.
- The game ends if the snake collides with the boundaries or itself.
- Press 'Q' to quit the game or 'C' to play again after the game ends.

## Game Features

- Responsive snake movement controlled by arrow keys.
- Randomly generated food positions.
- Snake growth and score tracking.
- Collision detection with boundaries and self-collision.
- End game screen with options to quit or play again.

## Code Structure

The code is structured into the following main components:

- `Snake` class: Represents the snake and handles its movement, growth, and collision detection.
- `Food` class: Represents the food and handles its random position generation.
- `game_loop` function: Implements the main game loop, handling events, updating game state, and rendering.
- `message` function: Displays game over messages on the screen.

## Customization

You can customize various aspects of the game by modifying the following variables in the code:

- `window_width` and `window_height`: Adjust the size of the game window.
- `snake_block_size`: Change the size of each block that makes up the snake and food.
- `snake_speed`: Modify the speed of the snake's movement.
- Colors (`white`, `black`, `red`, `green`): Change the colors used for the snake, food, and background.

Feel free to experiment and make the game your own!

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).