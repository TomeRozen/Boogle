from ex12_utils import *


TRY_BOARD2 = [['N', 'I', 'C', 'P'],
             ['C', 'E', 'O', 'E'],
             ['W', 'N', 'I', 'C'],
             ['A', 'U', 'L', 'E'],
             ['W', 'E', 'L', 'L']]


TRY_BOARD = [['N', 'I', 'P', 'P'],
             ['C', 'E', 'O', 'F'],
             ['W', 'S', 'X', 'M'],
             ['A', 'U', 'L', 'B']]

SMALL_DICT = load_words_dict("simple_words.txt")

def test_load_words_dict():
    assert type(SMALL_DICT) == dict
    assert SMALL_DICT['ACCOASTED'] is True

def test_is_valid_path():
    assert is_valid_path(TRY_BOARD, [(0,0), (0,1), (1,0), (1,1)], SMALL_DICT) == "NICE"
    assert is_valid_path(TRY_BOARD, [(0,0), (3,0), (3,2), (3,1)], SMALL_DICT) is None
    assert is_valid_path(TRY_BOARD, [(0,0), (0,0), (1,1), (1,2)], SMALL_DICT) is None
    assert is_valid_path(TRY_BOARD, [(0,0), (0,1), (1,1), (0,1)], SMALL_DICT) is None
    assert is_valid_path(TRY_BOARD, [(0,0), (1,1), (2,2), (3,3)], SMALL_DICT) is None
    assert is_valid_path(TRY_BOARD, [(0,0), (0,1), (0,2), (0,3), (0,4)], SMALL_DICT) is None

def test_length_n_words():
    assert find_length_n_words(4, TRY_BOARD2, SMALL_DICT) == [('NICE', [(0, 0), (0, 1), (0, 2), (1, 1)]),
                                                             ('NICE', [(0, 0), (0, 1), (0, 2), (1, 3)]),
                                                             ('NICE', [(0, 0), (0, 1), (1, 0), (1, 1)]),
                                                             ('NICE', [(2, 1), (2, 2), (2, 3), (3, 3)]),
                                                             ('NICE', [(2, 1), (2, 2), (2, 3), (1, 3)]),
                                                             ('WELL', [(4, 0), (4, 1), (4, 2), (3, 2)]),
                                                             ('WELL', [(4, 0), (4, 1), (4, 2), (4, 3)]),
                                                             ('WELL', [(4, 0), (4, 1), (3, 2), (4, 2)]),
                                                             ('WELL', [(4, 0), (4, 1), (3, 2), (4, 3)])]


