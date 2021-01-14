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
    """
    The game class. practically unites the gui and the logics in the model.
    """
    def __init__(self):
        """
        initializes the class
        """
        self._model = BoggleModel()
        self._gui = BoggleGUI()
        self.end_time = None

        self._gui._start_button["command"] = self.start_action
        self._gui._submit_button["command"] = self.submission
        self._gui._del_button["command"] = self.del_cmd

    def create_key_cmd(self, row, col):
        """
        creates a function with appropriates signature to be function run by a
        key (letter) button
        :param row: key row
        :param col: key column
        :return: a function, that runs functions in model and in gui
        """
        def fun():
            self._model.key_clicked(row, col)
            self._gui.set_display(self._model.get_cur_seq())
        return fun

    def assign_key(self, row, col):
        """
        assigns the key with it's relevant text (from board) and command
        :param row: key row
        :param col: key column
        :return:
        """
        self._gui.conf_key(str(row)+","+str(col),
                           self._model.board[row][col],
                           self.create_key_cmd(row, col))

    def del_cmd(self):
        """
        function to be assigned as the delete button command
        :return:
        """
        self._model.del_clicked()
        self._gui.set_display(self._model.get_cur_seq())

    def submission(self):
        """
        function to be assigned as the command of the submit button.
        :return:
        """
        self._model.submit_word()
        self.set_all_displays()

    def set_all_displays(self):
        """
        holds together all displays updates needs  to be done on several
        occasions
        :return:
        """
        self._gui.set_dict_display("Your Words:\n"+"\n"
                                   .join(self._model._words_found))
        self._gui.set_score_display("Score: " + str(self._model._score))
        self._gui.set_display(self._model.get_cur_seq())

    def start_action(self):
        """
        holds all the actions that need to be done when hitting the start
        button
        :return:
        """
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
        """
        an animation function, that being re-run during the game, to present
        how much time is left
        :return:
        """
        if self.end_time is not None:
            self._gui._countdown_label["text"] = \
                self._model.get_countdown(self.end_time)
            if self._gui._countdown_label["text"] == "0:00:00":
                self.end_game()
        self._gui._main_window.after(60, self.timer)

    def end_game(self):
        """
        runs all actions that need to be run when game time is over
        :return:
        """
        if self._gui.end_game(self._model._score):
            self.start_action()
        else:
            self._gui.quit_game()

    def _color_keys(self):
        """
        Function that is being re run during the game, the present the keys
        that can be clicked right now, based on the previous button that has
        been clicked
        :return:
        """
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
        """
        runs all the functions that run the game
        :return:
        """
        self.timer()
        self._color_keys()
        self._gui.run()

if __name__ == "__main__":
    boggle_game = BoggleClass()
    boggle_game.run()