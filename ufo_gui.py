import tkinter as tk
from tkinter import messagebox

class Game:
    def __init__(self, master):
        self.master = master
        master.title("UFO and Ship Game")

        self.ship_col = -1
        self.ufo_col = -1
        self.missile_counter = 0

        # create frame for the player placement inputs and display
        self.input_frame = tk.Frame(self.master)
        self.input_frame.grid(row=0, column=0, columnspan=3)

        # all the input fields that are in the frame widget
        self.place_pieces_input()

        # create board and the frame
        self.board = [[' ' for _ in range(7)] for _ in range(7)]
        self.board_frame = tk.Frame(self.master)

        # self.move_left_btn
        # self.move_right_btn
        # self.move_down_btn
        # self.shoot_btn

    def place_pieces_input(self):
        # display a welcome and instruction msg at the top
        self.welcome_msg = tk.Label(self.input_frame, text="Weclome to the UFO and Ship Game!", font=("Helvetica", 25, "bold"))
        self.welcome_msg.grid(row=0, column=0, columnspan=3, padx=5, pady=(15, 0))

        self.instruction_msg = tk.Label(self.input_frame, text="Please state where you would like to place your players", font=("Helvetica", 15, "bold"))
        self.instruction_msg.grid(row=1, columnspan=3, pady=(0, 15))

        # input fields for the ship and UFO position
        self.ship_label = tk.Label(self.input_frame, text="Enter a ship column (1-7):")
        self.ship_label.grid(row=2, column=0, columnspan=3)
        self.ship_entry = tk.Entry(self.input_frame, highlightthickness=1)
        self.ship_entry.grid(row=3, column=0, columnspan=3)

        self.ufo_label = tk.Label(self.input_frame, text="Enter a UFO column (1-7):")
        self.ufo_label.grid(row=4, column=0, columnspan=3)
        self.ufo_entry = tk.Entry(self.input_frame, highlightthickness=1)
        self.ufo_entry.grid(row=5, column=0, columnspan=3)

        # submit btn that will call the pice_placement function to confirm that the values in the input field are valid
        # before displaying them on the board
        self.submit_btn = tk.Button(self.input_frame, text="Submit", command=self.piece_placement, padx=10, pady=5)
        self.submit_btn.grid(row=6, columnspan=3, pady=15)

    def piece_placement(self):
        try:
            # gets the input of which col to place the ship and UFO
            self.ship_col = int(self.ship_entry.get()) - 1
            self.ufo_col = int(self.ufo_entry.get()) - 1

            # if not valid input then show the error msg
            if (self.ship_col < 0 or self.ship_col > 6 or self.ufo_col < 0 or self.ufo_col > 6):
                raise ValueError

            # place the players at the valid input and call the display_board function to show the players on the board
            self.board[6][self.ship_col] = 'S'
            self.board[0][self.ufo_col] = 'U'
            
            self.dislpay_board()

        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a number between 1 and 7.")
    
    def dislpay_board(self):
        # clear the prev input frame from the screen
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        # display the frame for the board of the game
        self.board_frame.grid(row=0, column=0, columnspan=3)

        # loop through the rows and cols of the board to create btns for each cell
        for row in range(7):
            for col in range(7):
                # create btn for each cell and display the text corresponding to that cell (S, U, or ' ')
                button = tk.Button(self.board_frame, width=5, height=2, text=self.board[row][col])
                button.grid(row=row, column=col)

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
