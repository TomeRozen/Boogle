import tkinter as tki

class BoogleGUI:
    def __init__(self):
        root = tki.Tk()
        root.title("Boogle!")

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
        self.pack()

    def pack(self):
        self._outer_frame.pack(side=tki.TOP, fill=tki.Y, expand=True)
        self._display_label.pack(side=tki.TOP, fill=tki.BOTH)
        self._right_frame.pack(side=tki.RIGHT, fill=tki.BOTH, expand=True)
        self._countdown_label.pack(side=tki.TOP)
        self._start_button.pack(side=tki.BOTTOM)

    def run(self):
        self._main_window.mainloop()

    def get_start_button(self):
        return self._start_button

if __name__ == '__main__':
    bg = BoogleGUI()
    bg.run()