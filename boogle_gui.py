import tkinter as tki

REGULAR_COLOR = 'lightgray'
BUTTON_STYLE = {"font": ("Courier", 30),
                "borderwidth": 1,
                "bg": REGULAR_COLOR,
                    }

class BoogleGUI:
    def __init__(self):
        root = tki.Tk()
        root.title("Boogle!")
        root.resizable(False, False)
        self._main_window = root
        self._outer_frame = tki.Frame(root, bg="gray35",
                                      highlightbackground="gray26",
                                      highlightthickness=3)
        self._display_label = tki.Label(self._outer_frame, width=25)
        self._right_frame = tki.Frame(self._outer_frame, bg="gray35")
        self._countdown_label = tki.Label(self._right_frame, text="3:00:00",
                                          bg="SkyBlue3",
                                          highlightbackground="gray17",
                                          highlightthickness=1)
        self._start_button = tki.Button(self._outer_frame, text="Start",
                                       font=("Courier", 20), width=11,
                                       bg="green3")
        self._keys_frame = tki.Frame(self._outer_frame, bg="gray35")
        self._curr_seq_label = tki.Label(self._outer_frame, text="Hello")
        self._score_label = tki.Label(self._right_frame, text="Score: ")
        self._score_label_count =tki.Label(self._right_frame)
        self._dict_list_label = tki.Label(self._right_frame, text="Your Words:\n")
        self._submit_button = tki.Button(self._outer_frame, text="Submit Your Word", bg="green2")
        self.pack()

        self._keys = {}

    def pack(self):
        self._outer_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)
        self._display_label.pack(side=tki.TOP, fill=tki.BOTH)
        self._right_frame.pack(side=tki.RIGHT, fill=tki.Y, expand=True)
        self._countdown_label.pack(side=tki.TOP)
        self._start_button.pack(side=tki.BOTTOM)
        self._score_label.pack(side=tki.TOP, expand=False, fill=tki.BOTH)
        self._dict_list_label.pack(side=tki.TOP, expand=False, fill=tki.BOTH)
        self._curr_seq_label.pack(side=tki.TOP, expand=True, fill=tki.BOTH)

    def _create_buttons_in_lower_frame(self, board_size) -> None:
        for i in range(board_size):
            tki.Grid.columnconfigure(self._keys_frame, i, weight=1)  # type: ignore
            tki.Grid.rowconfigure(self._keys_frame, i, weight=1)  # type: ignore

        for i in range(board_size):
            for j in range(board_size):
                self._make_button("", i, j)

    def _make_button(self, button_char: str, row: int, col: int,
                     rowspan: int = 1, columnspan: int = 1) -> tki.Button:
        button = tki.Button(self._keys_frame, text=button_char, **BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tki.NSEW)
        self._keys[str(row)+","+str(col)] = button
        return button

    def place_keys(self, board_size):
        self._keys_frame.pack(side=tki.BOTTOM, fill=tki.BOTH, expand=True)
        self._create_buttons_in_lower_frame(board_size)
        self._submit_button.pack(side=tki.TOP, expand=True, fill=tki.X)

    def get_key(self, location):
        return self._keys[location]

    def set_key_text(self, key_name, txt):
        self._keys[key_name].configure(text=txt)

    def run(self):
        self._main_window.mainloop()

    def get_start_button(self):
        return self._start_button

if __name__ == '__main__':
    bg = BoogleGUI()
    bg.run()