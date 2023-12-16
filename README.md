# tic-tac-toe-game-
my final project for Almdrasa Python Course, the game designed as PLayer Vs. PC
## Overview
This documentation outlines the structure and functionality of a Tic Tac Toe game implemented in Python using the Tkinter library. The game features a player versus computer mode where the player competes against a randomly moving computer opponent.

## Code Structure and Description

### Import Statements
- Tkinter for GUI elements.
- Font from Tkinter for custom font styling.
- Random for randomizing computer moves.

### GUI Initialization
- Creation of the main Tkinter window.
- Setting the title and making the window non-resizable.

### State Variables
- `players`: A list containing the symbols "X" and "O" representing the players.
- `turn`: A counter for the number of turns taken.
- `game_over`: A boolean flag indicating if the game has ended.
- `score_player`: An integer tracking the player's score.
- `score_pc`: An integer tracking the computer's score.

### Board Initialization
- `buttons`: A 3x3 grid of buttons representing the Tic Tac Toe board.

### Functions
#### start_new_game()
- Initializes a new game session.
- Randomly selects who starts first.
- Calls `restart()` to reset the game state.

#### disable_btns()
- Disables all the buttons on the board, used when the game ends.

#### check_winner()
- Checks for a winner or a tie after each move.
- Highlights winning combination and sets `game_over` flag.

#### update_scores(winner)
- Updates the score based on the winner of the game.

#### restart()
- Resets the game to its initial state for a new round.

#### switch_players()
- Switches the turn between the player and the computer.

#### computer_move()
- Automatically performs a move for the computer.

#### handle_game_over(winner)
- Handles actions to be taken once the game is over.

#### play_game(row, col)
- Manages a player's move and updates the board accordingly.

### GUI Components
#### Score Frame and Labels
- Displaying scores of the player and the computer.

#### Status Frame
- Shows the current status of the game (e.g., who's winning).

#### Restart Button
- Button to restart the game.

#### Game Board
- The 3x3 grid of buttons for playing Tic Tac Toe.

### Game Initialization
- Starts a new game and runs the main application loop.

## Conclusion
This documentation provides an insight into the functional aspects of the Tic Tac Toe game, explaining the core components and their roles in the overall gameplay.

