from boogle_model import BoogleModel
from boogle_gui import BoogleGUI
from boggle_board_randomizer import *
from datetime import timedelta

GAME_MINUTES = 3
BOARD_SIZE = 4
GOOD_KEY_COLOR = "DarkOliveGreen2"
BAD_KEY_COLOR = "coral1"
REGULAR_COLOR = 'lightgray'


class BoogleClass:
    def __init__(self):
        self._model = BoogleModel()
        self._gui = BoogleGUI()
        self._board = None
        self.end_time = None
        self.cur_seq = ""

        self._gui._start_button["command"] = self.start_action
        self._gui._submit_button["command"] = self.submission
        self._gui._del_button["command"] = self.del_cmd()

    def create_key_cmd(self, row, col):
        def fun():
            self._model.key_clicked(row, col)
            self._gui.set_display(self._model.get_cur_seq())
        return fun

    def del_cmd(self):
        def del_func():
            self._model.del_clicked()
            self._gui.set_display(self._model.get_cur_seq())
        return del_func

    def assign_key(self, row, col):
        self._gui.conf_key(str(row)+","+str(col),
                           self._model.board[row][col],
                           self.create_key_cmd(row, col))

    def submission(self):
        self._model.submit_word()
        self._gui.set_dict_display("Your Words:\n"+"\n"
                                   .join(self._model._words_found))
        self._gui.set_score_display("Score: " + str(self._model._score))
        self._gui.set_display("")

    def start_action(self):
        self.end_time = self._model.calc_end_time(GAME_MINUTES)
        self._model.reset_all()
        self._model.set_score()
        self._model.set_words_found_list()

        self._gui.set_dict_display("Your Words:\n")
        self._gui.set_score_display("Score: 0")
        self._gui.set_display(self._model.get_cur_seq())

        self._model.board = randomize_board()
        self._gui.place_keys(BOARD_SIZE)
        for row in range(len(self._model.board)):
            for col in range(len(self._model.board[0])):
                self.assign_key(row, col)

        self._gui._start_button["text"] = "Re-start!"
        self._gui._start_button["bg"] = "tomato"

    def _animate(self):
        if self.end_time is not None:
            self._gui._countdown_label["text"] = \
                self._model.get_countdown(self.end_time)
            if self._gui._countdown_label["text"] == "0:00:00":
                self.end_game()
        self._gui._main_window.after(60, self._animate)

    def end_game(self):
        if self._gui.end_game(self._model._score):
            self.start_action()
        else:
            self._gui.quit_game()

    def _color_keys(self):
        if self._model.board is not None:
            for row in range(len(self._model.board)):
                for col in range(len(self._model.board[0])):
                    if self._model.legal_locations():
                        if (row, col) in self._model.legal_locations() and \
                                (row, col) not in \
                                self._model.get_keys_pressed():
                            self._gui.conf_key_color(str(row) + "," + str(col),
                                                     GOOD_KEY_COLOR)
                        else:
                            self._gui.conf_key_color(str(row) + "," + str(col),
                                                     BAD_KEY_COLOR)
                    else:
                        self._gui.conf_key_color(str(row) + "," + str(col),
                                                 REGULAR_COLOR)
        self._gui._main_window.after(60, self._color_keys)

    def run(self):
        self._animate()
        self._color_keys()
        self._gui.run()

if __name__ == "__main__":
    boogle_game = BoogleClass()
    boogle_game.run()