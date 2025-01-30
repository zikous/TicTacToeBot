# Tic Tac Toe Game with AI

A Python implementation of the classic Tic Tac Toe game featuring a graphical user interface and an AI opponent using the Minimax algorithm.

## Overview

This project implements a Tic Tac Toe game where a human player (X) plays against an AI opponent (O). The game features a graphical interface built with Tkinter and uses the Model-View-Controller (MVC) architectural pattern.

## Features

- Graphical user interface with clickable buttons
- AI opponent using Minimax algorithm with alpha-beta pruning
- Score tracking for both players
- Restart game functionality
- Win/tie detection
- Clean, modular code structure using MVC pattern

## Project Structure

```
TicTacToeBot/
│
├── model.py         # Game logic and state management
├── view.py         # GUI implementation
├── controller.py   # Game control and coordination
├── agent.py       # AI opponent implementation
├── main.py        # Entry point
├── requirements.txt # Project dependencies
└── .gitignore     # Git ignore rules
```

## Installation

1. Clone the repository:

```bash
git https://github.com/zikous/TicTacToeBot
cd TicTacToeBot
```

2. Create and activate a virtual environment (recommended):

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Unix/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Install requirements:

```bash
pip install -r requirements.txt
```

## Requirements

- Python 3.x
- Tkinter >=8.6 (usually comes with Python installation)
- python-dateutil >=2.8.2

## How to Play

1. Run the game:

```python
python main.py
```

2. Game Rules:

   - You play as X, and the AI plays as O
   - Click on any empty square to make your move
   - The AI will automatically make its move after yours
   - First player to get three in a row (horizontal, vertical, or diagonal) wins
   - If no player wins and the board is full, the game is a tie

3. Controls:
   - Click squares to make moves
   - Use the "Restart" button to start a new game
   - Score is tracked automatically

## Code Structure

### Model (model.py)

- Manages game state and rules
- Handles the game board representation
- Tracks scores and current player
- Provides methods for making moves and checking game status

### View (view.py)

- Implements the graphical interface using Tkinter
- Displays the game board, scores, and messages
- Handles user input through button clicks
- Updates the display based on game state

### Controller (controller.py)

- Coordinates between Model and View
- Handles game flow and turn management
- Processes user input and AI moves
- Updates game state and view accordingly

### Agent (agent.py)

- Implements the AI opponent using Minimax algorithm
- Includes alpha-beta pruning for better performance
- Evaluates board positions
- Makes strategic decisions for optimal play

## Development Setup

1. Ensure you have Python 3.x installed
2. Install the required dependencies using `pip install -r requirements.txt`
3. Make sure your IDE/editor respects the .gitignore file
4. Run tests before submitting any changes

## Future Improvements

Potential enhancements that could be added:

- Difficulty levels for AI
- Custom board sizes
- Network multiplayer
- Game replay feature
- Save/load functionality

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.
