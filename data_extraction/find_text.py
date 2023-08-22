def get_specific_line(path: str, line_num: int) -> str:
    """
    Finds the sentence in a file in a specific line
    :param path: The path to the file
    :param line_num: The line number
    :return: The sentence in the line
    """
    with open(path, 'r', errors='ignore') as data_file:
        lines = data_file.readlines()

    return lines[line_num] if line_num < len(lines) else ''
