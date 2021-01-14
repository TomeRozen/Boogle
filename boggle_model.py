from typing import Tuple, List
from ex12_utils import *
from datetime import datetime, timedelta

DICT_FILE = "boggle_dict.txt"
START_SCORE = 0

class BoggleModel:
    """
    The model class implements logics of the game, especially keys commands 
    etc. 
    """
    def __init__(self):
        """
        initializes the class
        """
        self._words_dict = load_words_dict(DICT_FILE)
        self._words_found = list()
        self._score = START_SCORE
        self.board = None

    def reset_all(self):
        """
        reset parameters of model, to be run when needed in several occurrences
        :return: 
        """
        self._cur_seq = ""
        self._prev_button = ""
        self._keys_pressed = []

    def submit_word(self):
        """
        to be run when submit word button is pressed. submit the word currently
        being built, and does relevant actions
        :return: 
        """
        if self._cur_seq in self._words_dict:
            if self._cur_seq not in self._words_found:
                self._words_found.append(self._cur_seq)
                self._score += len(self._cur_seq) ** 2
        self.reset_all()

    def legal_locations(self):
        """
        returns all valid locations, coordinates on the board available for the
        next turn of the user, based on previous button pressed by him
        :return: False if all keys are valid, list of valid coordinates 
        otherwise
        """
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
        """
        function to be run when a key has been clicked by the user. updates the
        current sequence, and updates the prev_button variable.
        :param row: row of key pressed on the board
        :param col: column of key pressed on the board 
        :return: 
        """
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
        """
        function to be run when the delete button has been clicked. goes back
        one step in the sequence, keys_pressed variable and prev_button 
        :return: 
        """
        if self._cur_seq:
            self._cur_seq = self._cur_seq[:-len(self.board[self._prev_button[0]][self._prev_button[1]])]
            if self._keys_pressed:
                self._prev_button = self._keys_pressed.pop()
            else:
                self._prev_button = ""

    def calc_end_time(self, game_time):
        """
        calculates and returns the end time based on current time and game time
        :param game_time: length of game in minutes
        :return: time of game end
        """
        return datetime.now() + timedelta(minutes=game_time)

    def get_countdown(self, end_time):
        """
        returns a string represents time left for the game. 
        :param end_time: game end time
        :return: string represents how much time is left
        """
        left_time = end_time - datetime.now()
        if left_time < timedelta(minutes=0):
            return "0:00:00"
        return str(left_time)[3:7]+":"+str(left_time)[8:10]

    def get_cur_seq(self):
        """
        getter function for the current sequence
        :return: 
        """
        return self._cur_seq

    def get_prev_button(self):
        """
        getter function for the previous button
        :return: 
        """
        return self._prev_button

    def get_keys_pressed(self):
        """
        getter function for the keys pressed list
        :return: 
        """
        return self._keys_pressed

    def reset_score(self):
        """
        reset the game score
        :return: 
        """
        self._score = 0

    def reset_words_found_list(self):
        """
        reset the words that has been found list
        :return: 
        """
        self._words_found = []
