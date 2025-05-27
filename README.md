# AI-Powered Snake Game

## Project Overview

This project implements a classic Snake game where the snake is controlled by an Artificial Intelligence agent. The agent learns to play the game using a Reinforcement Learning technique called Q-learning. As the agent plays more games, it improves its strategy to maximize its score by eating food and avoiding collisions.

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
- Pygame (`pygame==2.5.2`)
- NumPy (`numpy==1.26.4`)
- PyTorch (`torch==2.2.2`)

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
python agent.py
```
This command will start the AI training process. You will see the game window and a plot of the training progress.

## How the AI Learns

This project demonstrates a Snake game where the snake is controlled by an AI agent. The agent learns to play the game through a process called Reinforcement Learning, specifically using a Q-learning algorithm. Here's a brief overview:

*   **Goal:** The agent's goal is to maximize its total score by eating food (the red squares) and avoiding collisions with the game window boundaries or its own body.
*   **Learning Process:**
    *   **State:** The agent observes the current game situation (its "state"), which includes information like the position of its head, the direction of movement, the location of the food, and immediate dangers around it.
    *   **Action:** Based on its current state and what it has learned, the agent chooses an action: to move straight, turn left, or turn right relative to its current direction.
    *   **Reward:** After performing an action, the agent receives a reward (or penalty):
        *   A positive reward for eating food.
        *   A negative reward (penalty) for colliding and ending the game.
        *   A small or no reward for just surviving.
    *   **Q-learning:** The agent uses a Q-network (a type of neural network defined in `model.py`) to estimate the expected future rewards for taking each possible action in a given state. It continuously updates these estimations as it plays more and more games, gradually learning which actions lead to better outcomes.
*   **Training:** When you run `python agent.py`:
    *   The AI agent starts playing the game. Initially, its moves might seem random.
    *   Over time, as it plays many games (epochs), it learns to make better decisions.
    *   The console will display the game number, current score, and the record score achieved so far.
    *   A plot will also be displayed, showing the scores per game and the mean scores, visualizing the agent's learning progress. The model (the agent's "brain") is saved periodically as `model.pth` in the `model` directory when a new record score is achieved.

## Training the Agent

When you execute `python agent.py`, the AI agent begins the training process:

1.  **Initialization**: The agent starts with no prior knowledge of the game (unless a pre-trained model is loaded, though the current script always starts training). Its Q-network (the "brain") has random weights.
2.  **Exploration vs. Exploitation**: Initially, the agent makes more random moves (exploration) to discover different strategies. As it gains experience (after a certain number of games, controlled by `self.epsilon` in `agent.py`), it starts relying more on its learned knowledge to make moves that it believes will yield higher rewards (exploitation).
3.  **Learning Loop**:
    *   The agent plays the Snake game repeatedly.
    *   In each game, it observes the state, chooses an action, receives a reward (or penalty), and observes the new state.
    *   This experience (state, action, reward, new state, game_over_status) is stored in its memory.
    *   The agent periodically samples batches of experiences from its memory to train its Q-network (this is called experience replay). This helps the agent learn from past experiences and stabilize the learning process.
    *   The `train_short_memory` method trains on the most recent move, while `train_long_memory` trains on a batch of past moves.
4.  **Monitoring Progress**:
    *   The console will show the number of games played, the score for each game, and the highest score achieved so far (record).
    *   A live plot visualizes the score per game and the average score over time, providing insight into how well the agent is learning.
5.  **Saving the Model**: Whenever the agent achieves a new record score, its current Q-network model is saved to a file named `model.pth` inside a `model` directory (which is created if it doesn't exist). This saved model contains the "learned knowledge" of the agent.

**Using a Trained Model**:

While the provided `agent.py` script is primarily for training, the saved `model.pth` file can be used to load a pre-trained agent. You would typically modify `agent.py` to load the weights from this file into the `Linear_QNet` model before starting the game if you wanted to see a trained agent in action without further training, or to resume training from a checkpoint. (The current script will always start training, but saves the best model it achieves during its run).

## Game Features

-   Snake game environment (`game.py`) suitable for reinforcement learning.
-   AI agent (`agent.py`) that learns to play Snake using Q-learning.
-   Deep Q-Network model (`model.py`) for action selection.
-   Real-time training progress displayed in the console (game number, score, record score).
-   Live plotting of scores and mean scores during training (`plotter.py`).
-   Automatic saving of the best performing model.
-   Randomly generated food positions.
-   Collision detection (boundaries and self-collision) handled by the game environment.
-   Score tracking and reward system for the AI agent.

## Code Structure

The project is organized into the following Python files:

-   `agent.py`: This is the main script to run. It contains the `Agent` class, which defines the reinforcement learning agent, manages the training loop, and interacts with the game environment. It handles the agent's memory, learning steps (short and long term), and action selection strategy.
-   `game.py`: Defines the `SnakeGameAI` class, which serves as the game environment. It manages the snake's movement, food placement, collision detection, score, and game state. It's designed to be controlled by an AI agent rather than a human player.
-   `model.py`: Contains the definition of the neural network (`Linear_QNet`) used by the AI agent. It also includes the `QTrainer` class, which handles the training of the neural network model using the Q-learning algorithm.
-   `plotter.py`: A utility script that uses `matplotlib` to generate a real-time plot of the agent's scores and mean scores during the training process, helping to visualize its learning progress.
-   `requirements.txt`: Lists the Python libraries required to run the project (Pygame, NumPy, PyTorch).

## Customization

You can customize various aspects of the game environment and the AI agent by modifying parameters in the code:

**Game Environment (`game.py`):**

*   `w` and `h` (in `SnakeGameAI.__init__`): Adjust the width and height of the game window. Note that changing dimensions might affect the agent's perception and may require retraining.
*   `BLOCK_SIZE`: Changes the size of each block for the snake and food. This also affects the game's grid size and could impact training.
*   `SPEED`: Modifies the game speed (frames per second). Higher speeds can make training faster but might be too challenging for the agent initially.
*   `GREEN`, `RED`, `BLACK`: Colors used for the snake, food, and background, respectively. These are primarily visual and shouldn't directly impact AI performance.

**AI Agent and Model (`agent.py`, `model.py`):**

*   `MAX_MEMORY` (in `agent.py`): The maximum size of the agent's experience replay memory.
*   `BATCH_SIZE` (in `agent.py`): The number of samples used in each training step for the long-term memory.
*   `LR` (Learning Rate, in `agent.py`): Controls how much the model's weights are updated during training.
*   `self.gamma` (Discount Factor, in `Agent.__init__`): Determines the importance of future rewards.
*   `hidden_size` (in `Linear_QNet.__init__` in `model.py`): The number of neurons in the hidden layer of the neural network. Modifying the network architecture will significantly impact learning.

**Note:** Modifying AI parameters (like learning rate, discount factor, network architecture, batch size, or memory size) can have a significant impact on the agent's learning ability and performance. It often requires experimentation to find optimal values. Changing game environment parameters like window size, block size, or speed might also necessitate retraining the agent.

## Technologies Used

*   **Python 3**: The core programming language used.
*   **Pygame**: A set of Python modules designed for writing video games. Used here to create the Snake game environment and visuals.
*   **PyTorch**: An open-source machine learning library used for building and training the neural network (Q-network) for the RL agent.
*   **NumPy**: A library for numerical computation in Python, used for handling game states and other numerical operations.
*   **Matplotlib**: A plotting library used by `plotter.py` to visualize the training progress.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).