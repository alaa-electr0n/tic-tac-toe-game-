import tkinter as tk
import tkinter.messagebox
import random

class TicTacToe:
    """A simple Tic Tac Toe game class using Tkinter."""

    def __init__(self, root):
        """Initialize the game with the main window and game variables."""
        self.root = root
        self.root.title("Tic Tac Toe")

        # Initialize player and computer scores
        self.player_score = 0
        self.computer_score = 0

        # Score label to display current scores
        self.score_label = tk.Label(root, text="You: 0 Computer: 0")
        self.score_label.grid(row=0, column=0, columnspan=3)

        # Create a 3x3 grid of buttons for the Tic Tac Toe game
        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text="", width=10, height=3, command=lambda i=i: self.player_move(i))
            button.grid(row=1 + i // 3, column=i % 3)
            self.buttons.append(button)

        # Restart button to reset the game
        self.restart_button = tk.Button(root, text="Restart", command=self.reset_game)
        self.restart_button.grid(row=4, column=0, columnspan=3)

        # Winning combinations for checking the game state
        self.winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]             # Diagonal
        ]

    def player_move(self, button_index):
        """Handle the player's move."""
        if self.buttons[button_index]['text'] == "":
            self.buttons[button_index]['text'] = "X"
            if not self.check_winner("X"):
                self.computer_move()

    def computer_move(self):
        """Handle the computer's move."""
        empty_buttons = [button for button in self.buttons if button['text'] == ""]
        if empty_buttons:
            random.choice(empty_buttons)['text'] = "O"
            self.check_winner("O")

    def check_winner(self, player):
        """Check if the current player has won the game."""
        for a, b, c in self.winning_combinations:
            if self.buttons[a]['text'] == self.buttons[b]['text'] == self.buttons[c]['text'] != "":
                if player == "X":
                    self.player_score += 1
                else:
                    self.computer_score += 1

                self.update_score()
                tkinter.messagebox.showinfo("Tic Tac Toe", f"'{player}' wins!")
                self.reset_game()
                return True

        if all(button['text'] != "" for button in self.buttons):
            tkinter.messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
            self.reset_game()
            return True

        return False

    def reset_game(self):
        """Reset the game by clearing all cells."""
        for button in self.buttons:
            button['text'] = ""

    def update_score(self):
        """Update the score display."""
        self.score_label['text'] = f"You: {self.player_score} Computer: {self.computer_score}"

# Create the main window and start the game
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
