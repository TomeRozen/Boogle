from boogle_model import BoogleModel
from boogle_gui import BoogleGUI
from boggle_board_randomizer import *
class BoogleClass:
    def __init__(self):
        self._model = BoogleModel()
        self._gui = BoogleGUI
        self._board = randomize_board()

if __name__ == "__main__":
    pass