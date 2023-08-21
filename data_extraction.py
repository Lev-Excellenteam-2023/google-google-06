import os
from re import findall

words_dict = {}


def remove_punctuation(input_string: str) -> str:
    """
    Removes punctuation from a string
    :param input_string: The string to remove punctuation from
    :return: The string without punctuation
    """
    output_string = findall('[A-Za-z0-9\t\s\n]', input_string)
    return ''.join(output_string)


def extract_data(path: str) -> None:
    """
    Extracts data from files in nested directories to a database (dictionary)
    :param path: The path to the file or directory
    """
    if os.path.isfile(path):
        with open(path, 'r', errors='ignore') as data_file:
            for line_num, line in enumerate(data_file):
                line = remove_punctuation(line)
                words = line.upper().split()
                for word_num, word in enumerate(words):
                    if word in words_dict:
                        if (path, line_num) in words_dict[word]:
                            words_dict[word][(path, line_num)].append(word_num)
                        else:
                            words_dict[word][(path, line_num)] = [word_num]
                    else:
                        words_dict[word] = {(path, line_num): [word_num]}
    elif os.path.isdir(path):
        for entry in os.listdir(path):
            extract_data(os.path.join(path, entry))
