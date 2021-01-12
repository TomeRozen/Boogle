from boogle_model import BoogleModel
from boogle_gui import BoogleGUI
from boggle_board_randomizer import *
from datetime import timedelta

GAME_MINUTES = 3
BOARD_SIZE = 4


class BoogleClass:
    def __init__(self):
        self._model = BoogleModel()
        self._gui = BoogleGUI()
        self._board = None
        self.end_time = None
        self.cur_seq = ""

        self._gui._start_button["command"] = self.start_action

    def create_key_cmd(self, row, col):
        def fun():
            self._model.key_clicked(row, col)
            self._gui.set_display(self._model.get_cur_seq())
        return fun

    def assign_key(self, row, col):
        self._gui.conf_key(str(row)+","+str(col),
                           self._model.board[row][col],
                           self.create_key_cmd(row, col))
        self._gui._submit_button["command"] = self._model.submit_word


    def assign_keys(self):
        for row in range(len(self._board)):
            for col in range(len(self._board[0])):
                self._gui.set_key_text(str(row)+","+str(col),
                                       self._board[row][col])

    def start_action(self):
        self.end_time = self._model.calc_end_time(GAME_MINUTES)
        self._model.reset_all()
        self._model.board = randomize_board()
        self._gui.place_keys(BOARD_SIZE)
        for row in range(len(self._model.board)):
            for col in range(len(self._model.board[0])):
                self.assign_key(row, col)
        self._gui._start_button["text"] = "Re-start!"
        self._gui._start_button["bg"] = "dark orange"

    def _animate(self):
        if self.end_time is not None:
            self._gui._countdown_label["text"] = \
                self._model.get_countdown(self.end_time)
        self._gui._main_window.after(60, self._animate)


    def display(self):
        # self._gui._curr_seq_label["text"] = self._model.get_cur_seq()
        self._gui._score_label["text"] = "Score: " + str(self._model._score)
        self._gui._dict_list_label["text"] = "\n".join(self._model._words_found)

        self._gui._main_window.after(60, self.display)

    def run(self):
        self._animate()
        self.apply_word_submittion()
        self._gui.run()

if __name__ == "__main__":
    boogle_game = BoogleClass()
    boogle_game.run()