from boggle_model import BoggleModel
from boggle_gui import BoggleGUI
from boggle_board_randomizer import *
from datetime import timedelta

GAME_MINUTES = 3
BOARD_SIZE = 4
GOOD_KEY_COLOR = "DarkOliveGreen2"
BAD_KEY_COLOR = "coral1"
REGULAR_COLOR = 'tan1'


class BoggleClass:
    def __init__(self):
        self._model = BoggleModel()
        self._gui = BoggleGUI()
        self.end_time = None

        self._gui._start_button["command"] = self.start_action
        self._gui._submit_button["command"] = self.submission
        self._gui._del_button["command"] = self.del_cmd

    def create_key_cmd(self, row, col):
        def fun():
            self._model.key_clicked(row, col)
            self._gui.set_display(self._model.get_cur_seq())
        return fun

    def assign_key(self, row, col):
        self._gui.conf_key(str(row)+","+str(col),
                           self._model.board[row][col],
                           self.create_key_cmd(row, col))

    def del_cmd(self):
        self._model.del_clicked()
        self._gui.set_display(self._model.get_cur_seq())

    def submission(self):
        self._model.submit_word()
        self.set_all_displays()

    def set_all_displays(self):
        self._gui.set_dict_display("Your Words:\n"+"\n"
                                   .join(self._model._words_found))
        self._gui.set_score_display("Score: " + str(self._model._score))
        self._gui.set_display(self._model.get_cur_seq())

    def start_action(self):
        self.end_time = self._model.calc_end_time(GAME_MINUTES)

        self._model.reset_all()
        self._model.reset_score()
        self._model.reset_words_found_list()

        self.set_all_displays()

        self._model.board = randomize_board()
        self._gui.place_keys(BOARD_SIZE)
        for row in range(len(self._model.board)):
            for col in range(len(self._model.board[0])):
                self.assign_key(row, col)

        self._gui.start_button_reshape()

    def timer(self):
        if self.end_time is not None:
            self._gui._countdown_label["text"] = \
                self._model.get_countdown(self.end_time)
            if self._gui._countdown_label["text"] == "0:00:00":
                self.end_game()
        self._gui._main_window.after(60, self.timer)

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
        self.timer()
        self._color_keys()
        self._gui.run()

if __name__ == "__main__":
    boggle_game = BoggleClass()
    boggle_game.run()