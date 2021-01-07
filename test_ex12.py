from ex12_utils import *

def test_load_words_dict()
    dict_words = load_words_dict("simple_words.txt")
    assert type(dict_words) == dict
    assert a