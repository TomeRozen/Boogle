from typing import List, Tuple, Dict
MIN_COORD = 0
MAX_COORD = 3

def load_words_dict(file_path):
    words_dict = {}
    with open(file_path) as file:
        for line in file.readlines():
            words_dict[line.strip()] = True
    return words_dict


def is_valid_path(board: List[List[str]], path: List, words: Dict):
    word = ""
    for index, location in enumerate(path):
        if path.count(location) > 1:
            return
        for ind, coord in enumerate(location):
            if coord > MAX_COORD or coord < MIN_COORD:
                return
            if index > 0:
                if coord - path[index-1][ind] > 1 or \
                        coord - path[index-1][ind] < -1:
                    return

        letter = board[location[0]][location[1]]
        word += letter
    if word.upper() in words:
        return word




def find_length_n_words(n, board, words):
    pass