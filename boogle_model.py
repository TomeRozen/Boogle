from ex12_utils import *
from datetime import datetime, timedelta
class BoogleModel:
    def __init__(self):
        self._words_dict = load_words_dict("boggle_dict.txt")
        self._words_found = list()
        self._score = 0

    def add_letter(self, word, letter):
        new_word = word + letter
        return new_word

    def submit_word(self, word):
        if seq in self._words_dict:
            if seq not in self._words_found:
                self._words_found.append(word)
                self._score += len(word) ** 2

    def legal_locations(self, location):
        list_of_locations = []
        # for

    def calc_end_time(self, game_time):
        return datetime.now() + timedelta(minutes=game_time)

    def get_countdown(self, end_time):
        left_time = end_time - datetime.now()
        return str(left_time)[3:7]+":"+str(left_time)[8:10]



