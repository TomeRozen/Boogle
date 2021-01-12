from ex12_utils import *
from datetime import datetime, timedelta
class BoogleModel:
    def __init__(self):
        self._words_dict = load_words_dict("boggle_dict.txt")
        self._words_found = ["elinoy"]
        self._score = 0
        self._cur_seq = "ABET"

    def add_letter(self, word, letter):
        new_word = word + letter
        return new_word

    def submit_word(self):
        if self._cur_seq in self._words_dict:
            if self._cur_seq not in self._words_found:
                self._words_found.append(self._cur_seq)
                self._score += len(self._cur_seq) ** 2
                self._cur_seq = ""

    def legal_locations(self, location):
        list_of_locations = []
        # for

    def calc_end_time(self, game_time):
        return datetime.now() + timedelta(minutes=game_time)

    def get_countdown(self, end_time):
        left_time = end_time - datetime.now()
        return str(left_time)[3:7]+":"+str(left_time)[8:10]

    def get_cur_seq(self):
        return self._cur_seq

