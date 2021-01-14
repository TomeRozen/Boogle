from typing import Tuple, List
from ex12_utils import *
from datetime import datetime, timedelta

DICT_FILE = "boggle_dict.txt"
START_SCORE = 0

class BoggleModel:
    def __init__(self):
        self._words_dict = load_words_dict(DICT_FILE)
        self._words_found = list()
        self._score = START_SCORE
        self.board = None

    def reset_all(self):
        self._cur_seq = ""
        self._prev_button = ""
        self._keys_pressed = []

    def submit_word(self):
        if self._cur_seq in self._words_dict:
            if self._cur_seq not in self._words_found:
                self._words_found.append(self._cur_seq)
                self._score += len(self._cur_seq) ** 2
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
            possible_moves) and cur_key not in \
                self._keys_pressed:
            self._cur_seq += self.board[row][col]

            if self._prev_button:
                self._keys_pressed.append(self._prev_button)

            self._prev_button = (row, col)

    def del_clicked(self):
        if self._cur_seq:
            self._cur_seq = self._cur_seq[:-len(self.board[self._prev_button[0]][self._prev_button[1]])]
            if self._keys_pressed:
                self._prev_button = self._keys_pressed.pop()
            else:
                self._prev_button = ""

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

    def reset_score(self):
        self._score = 0

    def reset_words_found_list(self):
        self._words_found = []
