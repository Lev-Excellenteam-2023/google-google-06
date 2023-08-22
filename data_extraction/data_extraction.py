import os
from re import findall
from typing import Dict, List, Tuple


def remove_punctuation(input_string: str) -> str:
    """
    Removes punctuation from a string
    :param input_string: The string to remove punctuation from
    :return: The string without punctuation
    """
    output_string = findall('[A-Za-z0-9\t\s\n]', input_string)
    return ''.join(output_string)


def get_files_names(path: str) -> List[str]:
    """
    Gets the names of all the files in a directory and its subdirectories
    :param path: The path to the root directory
    :return: A list containing the names of all the files in the directory and its subdirectories
    """
    files_list = []
    if os.path.isfile(path):
        return [path]
    for root, dirs, files in os.walk(path):
        files_list += [os.path.join(root, file) for file in files]
    return files_list


def extract_data(root: str) -> Dict[str, Dict[Tuple[str, int], List[int]]]:
    """
    Extracts data from files of root and files of its subdirectories
    :param root: The path to the root directory
    :return: A dictionary containing the data, where the keys are the words and the values are dictionaries
    containing the path to the file, line numbers and the offset numbers of the occurrences of the word
    """
    words_dict = {}
    files = get_files_names(root)
    for file in files:
        with open(file, 'r', errors='ignore') as data_file:
            for line_num, line in enumerate(data_file):
                line = remove_punctuation(line)
                words = line.upper().split()
                for word_num, word in enumerate(words):
                    if word in words_dict:
                        if (file, line_num) in words_dict[word]:
                            words_dict[word][(file, line_num)].append(word_num)
                        else:
                            words_dict[word][(file, line_num)] = [word_num]
                    else:
                        words_dict[word] = {(file, line_num): [word_num]}

    return words_dict
