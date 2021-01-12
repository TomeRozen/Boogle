from typing import Tuple
from ex12_utils import *
from datetime import datetime, timedelta
class BoogleModel:
    _cur_seq: str
    _prev_button: Tuple
    _cur_display: str

    def __init__(self):
        self._words_dict = load_words_dict("boggle_dict.txt")
        self._words_found = list()
        self._score = 0
        self.board = None

    def reset_all(self):
        self._cur_seq = ""
        self._prev_button = ""
        self._cur_display = ""

    def add_letter(self, word, letter):
        new_word = word + letter
        return new_word

    def submit_word(self):
        if self._cur_seq in self._words_dict:
            if self._cur_seq not in self._words_found:
                print(self._cur_seq)
                self._words_found.append(self._cur_seq)
                self._score += len(self._cur_seq) ** 2
                self.reset_all()
        else:
            self.reset_all()


    def legal_locations(self, location):
        legal_locations = []
        if self._prev_button == "":
            return -1
        else:
            cur_row = location[0]
            cur_col = location[1]
            legal_locations.extend([(cur_row, cur_col-1), (cur_row, cur_col+1),
                                   (cur_row-1, cur_col-1), (cur_row-1, cur_col),
                                   (cur_row-1, cur_col+1), (cur_row+1, cur_col-1),
                                    (cur_row+1, cur_col), (cur_row+1, cur_col+1)])
            return legal_locations
            

    def key_clicked(self, row, col):
        possible_moves = self.legal_locations(self._prev_button)
        if possible_moves == -1 or (row, col) in self.legal_locations(self._prev_button):
            if self._cur_seq is None:
                self._cur_seq = self.board[row][col]
            else:
                self._cur_seq += self.board[row][col]
            self._prev_button = (row, col)
        
    def calc_end_time(self, game_time):
        return datetime.now() + timedelta(minutes=game_time)

    def get_countdown(self, end_time):
        left_time = end_time - datetime.now()
        return str(left_time)[3:7]+":"+str(left_time)[8:10]

    def get_cur_seq(self):
        return self._cur_seq

