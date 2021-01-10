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
    paths_list = []
    for word in words:
        if len(word) == n:
            word_paths = []
            for row_ind, row in enumerate(board):
                for col_ind, col in enumerate(row):
                    if board[row_ind][col_ind][0] == word[0]:
                        word_paths = _helper_find_length(board, word, row_ind, col_ind, word_paths, [], "")
            if word_paths != []:
                for path in word_paths:
                    paths_list.append((word,path))
    return paths_list

def _helper_find_length(board, word, row_ind, col_ind, word_paths, cur_path, seq):
    cur_path.append((row_ind, col_ind))
    seq = seq+board[row_ind][col_ind]

    if seq != word[:len(seq)]:
        cur_path.pop(-1)
        return
    if len(seq) > len(word):
        cur_path.pop(-1)
        return
    if len(seq) == len(word):
        if seq == word:
            word_paths.append(cur_path)
            return

    if row_ind < len(board)-1:
        _helper_find_length(board, word, row_ind + 1, col_ind, word_paths, cur_path,
                        seq)

    if row_ind > 0:
        _helper_find_length(board, word, row_ind - 1, col_ind, word_paths,  cur_path,
                        seq)

    if col_ind < len(board[0]) -1:
        _helper_find_length(board, word, row_ind, col_ind + 1, word_paths,  cur_path,
                        seq)

    if col_ind > 0:
        _helper_find_length(board, word, row_ind, col_ind - 1, word_paths,   cur_path,
                        seq)


    # up + left:
    if row_ind > 0 and col_ind > 0:
        _helper_find_length(board, word, row_ind - 1, col_ind - 1, word_paths,   cur_path,
                        seq)


    # up + right:
    if row_ind > 0 and col_ind < len(board[0]) -1:
        _helper_find_length(board, word, row_ind - 1, col_ind + 1, word_paths, cur_path,
                        seq)


    # down + left:
    if row_ind < len(board) -1 and col_ind > 0:
        _helper_find_length(board, word, row_ind + 1, col_ind - 1, word_paths,  cur_path,
                        seq)

    # down + right:
    if row_ind < len(board) -1 and col_ind < len(board[0]) -1:
        _helper_find_length(board, word, row_ind + 1, col_ind + 1, word_paths,  cur_path,
                        seq)

    return word_paths







