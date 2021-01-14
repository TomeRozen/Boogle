import tkinter as tki
from tkinter import messagebox

REGULAR_COLOR = 'tan1'
BUTTON_STYLE = {"font": ("Comic Sans MS", 20),
                "borderwidth": 1,
                "bg": REGULAR_COLOR}
START_BUTTON_RESHAPE = {"text": "Re-start!", "bg": "OrangeRed2",
                                     "width": 19, "height": 1,
                        "font": ("Comic Sans MS", 18)}
OUTER_FRAME_STYLE = {"bg": "sienna1",
                    "highlightbackground": "sienna1",
                    "highlightthickness": 3}
DISPLAY_FRAME_STYLE = {"bg":"sienna1", "highlightbackground": "sienna1",
                                      "highlightthickness": 3}
COUNT_LABEL_STYLE = {"text": "00:00:00",
                    "bg": "SeaGreen1",
                    "highlightbackground": "sienna1",
                    "highlightthickness": 1, "font": ("Comic Sans MS", 10)}
START_BUTTON_STYLE = {"text":"Start", "width":8, "height":3,
               "bg":"lawn green", "font":("Comic Sans MS", 50)}
SCORE_LABEL_STYLE = {"text": "Score: 0", "bg": "green yellow",
                     "font": ("Comic Sans MS", 10)}
DICT_LABEL_STYLE = {"text": "Your Words:\n", "bg": "gold2",
                    "font": ("Comic Sans MS", 10)}
SUBMIT_STYLE = {"text":"Submit Your Word", "bg": "chartreuse2",
                "font": ("Comic Sans MS", 10)}
DEL_STYLE = {"text": "del", "bg": "coral1",
             "font": ("Comic Sans MS", 10)}

class BoggleGUI:
    """
    Packs all of the games GUI's functions and initializes it.
    """
    def __init__(self):
        """
        Initializing the games buttons and frames, and packing them into the
        main window.
        """
        root = tki.Tk()
        root.title("Boggle!")
        root.resizable(False, False)
        self._main_window = root
        self._outer_frame = tki.Frame(root, **OUTER_FRAME_STYLE)
        self._display_frame = tki.Frame(self._outer_frame,
                                        **DISPLAY_FRAME_STYLE)
        self._display_label = tki.Label(self._display_frame, width=25,
                                        bg="tan1")
        self._right_frame = tki.Frame(self._outer_frame, bg="sienna1")
        self._countdown_label = tki.Label(self._right_frame,
                                          **COUNT_LABEL_STYLE)
        self._start_button = tki.Button(self._outer_frame,
                                        **START_BUTTON_STYLE)
        self._keys_frame = tki.Frame(self._outer_frame, bg="sienna1")
        self._score_label = tki.Label(self._right_frame, **SCORE_LABEL_STYLE)
        self._dict_list_label = tki.Label(self._right_frame,
                                          **DICT_LABEL_STYLE)
        self._submit_button = tki.Button(self._outer_frame,**SUBMIT_STYLE)
        self._del_button = tki.Button(self._display_frame, **DEL_STYLE)
        self.pack()

        self._keys = {}

    def pack(self):
        """
        a helper function for the init. packs all the buttons, labels and frames.

        """
        self._outer_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)
        self._display_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)
        self._display_label.pack(side=tki.LEFT, fill=tki.BOTH, expand=True)
        self._right_frame.pack(side=tki.RIGHT, fill=tki.Y, expand=True)
        self._countdown_label.pack(side=tki.TOP, fill=tki.BOTH)
        self._start_button.pack(side=tki.BOTTOM)
        self._score_label.pack(side=tki.TOP, fill=tki.BOTH)
        self._dict_list_label.pack(side=tki.TOP, fill=tki.BOTH)
        self._del_button.pack(side=tki.RIGHT)

    def _create_buttons_in_keys_frame(self, board_size) -> None:
        """
        Creates the letters buttons, by the wanted board size.

        """
        for i in range(board_size):
            tki.Grid.columnconfigure(self._keys_frame, i,
                                     weight=1)  # type: ignore
            tki.Grid.rowconfigure(self._keys_frame, i,
                                  weight=1)  # type: ignore

        for i in range(board_size):
            for j in range(board_size):
                self._make_button("", i, j)

    def _make_button(self, button_char: str, row: int, col: int,
                     rowspan: int = 1, columnspan: int = 1) -> tki.Button:
        """
        a helper function of the _create_buttons_in_keys_frame function.
        creates each button.

        """
        button = tki.Button(self._keys_frame, text=button_char, **BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan,
                    columnspan=columnspan, sticky=tki.NSEW)
        self._keys[str(row) + "," + str(col)] = button
        return button

    def place_keys(self, board_size):
        """
        Packs the letters buttons into the board

        """
        self._keys_frame.pack(side=tki.BOTTOM, fill=tki.BOTH, expand=True)
        self._create_buttons_in_keys_frame(board_size)
        self._submit_button.pack(side=tki.TOP, expand=True, fill=tki.X)

    def conf_key(self, key_name, txt, cmd):
        """
        configures a key.
        This function is called from the main class of the game when starting
        a new game.
        """
        self._keys[key_name].configure(text=txt, command=cmd)

    def conf_key_color(self, key_name, color):
        """
        configures the keys color based on the users current path.
        """
        self._keys[key_name].configure(bg=color)

    def start_button_reshape(self):
        """
        reshaping the start button into a "restart" button after
         the user started the game.
        """
        self._start_button.configure(**START_BUTTON_RESHAPE)

    def run(self):
        """ runs the GUIs main loop"""
        self._main_window.mainloop()

    def get_start_button(self):
        """ a getter to the start button"""
        return self._start_button

    def set_display(self, txt):
        """ setting the sequence's display after submitting a word"""
        self._display_label["text"] = txt

    def set_dict_display(self, txt):
        """ setting the dictionary's display after submitting a word"""
        self._dict_list_label["text"] = txt

    def set_score_display(self, txt):
        """ setting the score's display after submitting a word"""
        self._score_label["text"] = txt

    def end_game(self, score):
        """ pops a message to the user when the time is out, asking if he
        wants to play again or exit the game."""
        return tki.messagebox.askyesno(title="Game Over",
                            message="Time is out.\nYour Score is: " +
                            str(score) + "\nDo you want to play again?")

    def quit_game(self):
        """quits the game"""
        self._main_window.destroy()

# if __name__ == '__main__':
#     bg = boggleGUI()
#     bg.run()