import tkinter as tk
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [' '] * 9  # Representing the 3x3 board
        self.winner = None
        self.human_score = 0
        self.computer_score = 0
        self.current_player = None

        self.name_label = tk.Label(root, text="Enter your name:")
        self.name_label.grid(row=0, column=0, columnspan=3)

        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=3, columnspan=3)

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.grid(row=1, column=0, columnspan=6)

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(root, text='', font=('normal', 20), width=6, height=2,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i + 2, column=j, sticky='nsew')
                self.buttons.append(button)

        self.score_label = tk.Label(root, text="Scoreboard:")
        self.score_label.grid(row=2, column=4, columnspan=2, sticky='w')

        self.score_text = tk.StringVar()
        self.score_display = tk.Label(root, textvariable=self.score_text)
        self.score_display.grid(row=3, column=4, columnspan=2, sticky='w')

        self.message_label = tk.Label(root, text="Game Result:")
        self.message_label.grid(row=5, column=4, columnspan=2, sticky='w')

        self.message_text = tk.StringVar()
        self.message_display = tk.Label(root, textvariable=self.message_text)
        self.message_display.grid(row=6, column=4, columnspan=2, sticky='w')

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

    def start_game(self):
        player_name = self.name_entry.get()
        if not player_name:
            player_name = "Player"

        self.board = [' '] * 9
        self.winner = None
        self.current_player = random.choice(['X', 'O'])
        self.name_label.config(text=f"Welcome, {player_name}!")
        self.name_entry.config(state=tk.DISABLED)
        self.update_board()

    def make_move(self, row, col):
        index = 3 * row + col
        if self.board[index] == ' ' and not self.winner:
            self.board[index] = 'X'
            self.check_winner()
            if not self.winner:
                self.computer_move()
                self.check_winner()
            self.update_board()

    def computer_move(self):
        empty_cells = [i for i in range(9) if self.board[i] == ' ']
        if empty_cells:
            computer_choice = random.choice(empty_cells)
            self.board[computer_choice] = 'O'

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                if self.board[combo[0]] == 'X':
                    self.human_score += 1
                else:
                    self.computer_score += 1
                self.winner = self.board[combo[0]]
                self.display_winner()
                return

        if ' ' not in self.board:
            self.winner = 'Tie'
            self.display_winner()

    def display_winner(self):
        if self.winner == 'X':
            winner_text = f"{self.name_entry.get()} wins!"
        elif self.winner == 'O':
            winner_text = "Computer wins!"
        else:
            winner_text = "It's a tie!"

        winner_text += f"\n\n{self.name_entry.get()}: {self.human_score} | Computer: {self.computer_score}"
        self.message_text.set(winner_text)

        self.name_entry.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
        self.show_message("Game Over", winner_text)

    def show_message(self, title, message):
        popup = tk.Toplevel(self.root)
        popup.title(title)
        tk.Label(popup, text=message, padx=10, pady=10).pack()
        tk.Button(popup, text="OK", command=popup.destroy).pack()

    def update_board(self):
        for i in range(9):
            self.buttons[i].config(text=self.board[i])

        score_text = f"{self.name_entry.get()}: {self.human_score} | Computer: {self.computer_score}"
        self.score_text.set(score_text)

        if not self.winner:
            self.start_button.config(state=tk.DISABLED)
            self.name_entry.config(state=tk.DISABLED)
        else:
            self.start_button.config(state=tk.NORMAL)
            self.name_entry.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
