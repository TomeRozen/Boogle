from typing import Tuple, List
from ex12_utils import *
from datetime import datetime, timedelta

DICT_FILE = "boggle_dict.txt"

class BoogleModel:
    _cur_seq: str
    _prev_button: Tuple
    _cur_display: str
    _keys_pressed: List

    def __init__(self):
        self._words_dict = load_words_dict(DICT_FILE)
        self._words_found = list()
        self._score = 0
        self.board = None
        self._prev_button = ""

    def reset_all(self):
        self._cur_seq = ""
        self._prev_button = ""
        self._cur_display = ""
        self._keys_pressed = []

    def add_letter(self, word, letter):
        new_word = word + letter
        return new_word

    def submit_word(self):
        if self._cur_seq in self._words_dict:
            if self._cur_seq not in self._words_found:
                self._words_found.append(self._cur_seq)
                self._score += len(self._cur_seq) ** 2
                self.reset_all()
        else:
            self.reset_all()

    def legal_locations(self):
        legal_locations = []
        if self._prev_button == "":
            return False
        else:
            cur_row = self._prev_button[0]
            cur_col = self._prev_button[1]
            legal_locations.extend(
                [(cur_row, cur_col - 1), (cur_row, cur_col + 1),
                 (cur_row - 1, cur_col - 1), (cur_row - 1, cur_col),
                 (cur_row - 1, cur_col + 1), (cur_row + 1, cur_col - 1),
                 (cur_row + 1, cur_col), (cur_row + 1, cur_col + 1)])
            return legal_locations

    def key_clicked(self, row, col):
        possible_moves = self.legal_locations()
        cur_key = (row, col)
        if (possible_moves is False or cur_key in
            self.legal_locations()) and cur_key not in \
                self._keys_pressed:

            if self._cur_seq is None:
                self._cur_seq = self.board[row][col]
            else:
                self._cur_seq += self.board[row][col]

            self._prev_button = (row, col)
            self._keys_pressed.append(self._prev_button)

    def calc_end_time(self, game_time):
        return datetime.now() + timedelta(minutes=game_time)

    def get_countdown(self, end_time):
        left_time = end_time - datetime.now()
        if left_time < timedelta(minutes=0):
            return "0:00:00"
        return str(left_time)[3:7]+":"+str(left_time)[8:10]

    def get_cur_seq(self):
        return self._cur_seq

    def get_prev_button(self):
        return self._prev_button

    def get_keys_pressed(self):
        return self._keys_pressed
    def set_score(self):
        self._score = 0

    def set_words_found_list(self):
        self._words_found = []
