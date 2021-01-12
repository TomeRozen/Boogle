from boogle_model import BoogleModel
from boogle_gui import BoogleGUI
from boggle_board_randomizer import *
from datetime import timedelta

GAME_MINUTES = 3


class BoogleClass:
    def __init__(self):
        self._model = BoogleModel()
        self._gui = BoogleGUI()
        self._board = randomize_board()
        self.end_time = None

        self._gui._start_button["command"] = self.start_action

    def start_action(self):
        self.end_time = self._model.calc_end_time(GAME_MINUTES)

    def _animate(self):
        if self.end_time is not None:
            self._gui._countdown_label["text"] = \
                self._model.get_countdown(self.end_time)
        self._gui._main_window.after(60, self._animate)

    def run(self):
        self._animate()
        self._gui.run()

if __name__ == "__main__":
    boogle_game = BoogleClass()
    boogle_game.run()