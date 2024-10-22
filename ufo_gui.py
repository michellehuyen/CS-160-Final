import tkinter as tk
from tkinter import messagebox

class Game:
    def __init__(self, master):
        self.master = master
        master.title("UFO and Ship Game")

        self.ship_col = -1
        self.ufo_col = -1
        self.missile_counter = 0

        self.input_frame = tk.Frame(self.master)
        self.input_frame.grid(row=0, column=0, columnspan=3)

        self.place_pieces_input()

        # create board
        self.board = [[' ' for _ in range(7)] for _ in range(7)]
        self.board_frame = tk.Frame(self.master)

        # self.move_left_btn
        # self.move_right_btn
        # self.move_down_btn
        # self.shoot_btn

    def place_pieces_input(self):
        self.welcome_msg = tk.Label(self.input_frame, text="Weclome to the UFO and Ship Game!", font=("Helvetica", 25, "bold"))
        self.welcome_msg.grid(row=0, column=0, columnspan=3, padx=5, pady=(15, 0))

        self.instruction_msg = tk.Label(self.input_frame, text="Please state where you would like to place your players", font=("Helvetica", 15, "bold"))
        self.instruction_msg.grid(row=1, columnspan=3, pady=(0, 15))

        self.ship_label = tk.Label(self.input_frame, text="Enter a ship column (1-7):")
        self.ship_label.grid(row=2, column=0, columnspan=3)
        self.ship_entry = tk.Entry(self.input_frame, highlightthickness=1)
        self.ship_entry.grid(row=3, column=0, columnspan=3)

        self.ufo_label = tk.Label(self.input_frame, text="Enter a UFO column (1-7):")
        self.ufo_label.grid(row=4, column=0, columnspan=3)
        self.ufo_entry = tk.Entry(self.input_frame, highlightthickness=1)
        self.ufo_entry.grid(row=5, column=0, columnspan=3)

        self.submit_btn = tk.Button(self.input_frame, text="Submit", command=self.piece_placement, padx=10, pady=5)
        self.submit_btn.grid(row=6, columnspan=3, pady=15)

    def piece_placement(self):
        try:
            self.ship_col = int(self.ship_entry.get()) - 1
            self.ufo_col = int(self.ufo_entry.get()) - 1

            if (self.ship_col < 0 or self.ship_col > 6 or self.ufo_col < 0 or self.ufo_col > 6):
                raise ValueError

            self.board[6][self.ship_col] = 'S'
            self.board[0][self.ufo_col] = 'U'
            
            self.dislpay_board()

        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a number between 1 and 7.")
    
    def dislpay_board(self):
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        self.board_frame.grid(row=0, column=0, columnspan=3)

        for row in range(7):
            for col in range(7):
                button = tk.Button(self.board_frame, width=5, height=2, text=self.board[row][col])
                button.grid(row=row, column=col)

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
