from ex12_utils import *
from datetime import datetime, timedelta
class BoogleModel:
    def __init__(self):
        pass

    def add_letter(self, word, letter):
        new_word = word + letter
        return new_word

    def submit_word(self, board, path, words):
        word = is_valid_path(board, path, words)
        if word:
            pass

    def legal_locations(self, location):
        list_of_locations = []
        # for

    def calc_end_time(self):
        return datetime.now() + timedelta(minutes=3)

    def get_countdown(self, end_time):
        left_time = end_time - datetime.now()
        return str(left_time)[3:7]+":"+str(left_time)[8:10]