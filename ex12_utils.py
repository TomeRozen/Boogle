def load_words_dict(file_path):
    words_dict = {}
    with open(file_path) as file:
        for line in file.readlines():
            words_dict[line.strip()] = True
    return words_dict

print(load_words_dict("simple_words.txt"))

def is_valid_path(board, path, words):
    pass


def find_length_n_words(n, board, words):
    pass