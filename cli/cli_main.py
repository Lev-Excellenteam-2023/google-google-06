import re
import os
from dotenv import load_dotenv
from text_predictor.new_predictor import get_suggestions
from data_extraction.extract_data_to_dictionary import extract_data


root = os.getenv("ROOT_PATH")
if not root:
    load_dotenv()
    root = os.getenv("ROOT_PATH")


def just_uppercase(input_str: str) -> str:
    '''

    :param input_str: String with lowercase and uppercase letters, with non-letter characters, and with some whitespaces
                        between two words.
    :return: The same string with uppercase letters, without the non-letters characters, and with one whitespac between
                        the words in the string.
    '''
    upper_str = ''
    for char in input_str:
        if char.isalpha() or char == ' ':
            upper_str += char
        elif char == '\t':
            upper_str += ' '
    upper_str = re.sub(r'\s+', ' ', upper_str)
    return upper_str.upper()


def main():
    print('Loading the files and preparing the system...')
    data_structure = extract_data(root)
    print('The system is ready.\nThere is no need to pay attention to upper or lower case letters, or punctuation'
          'marks. '
          '\nTo reset the input enter #, to exit the program enter *.')
    user_input = input("Enter your input:\n")
    while user_input != '*':
        all_user_inputs = ''
        while user_input != '#' and user_input != '*':
            all_user_inputs += user_input
            upper_input = just_uppercase(all_user_inputs)
            suggestions = get_suggestions(data_structure, upper_input)
            if len(suggestions) > 0:
                print(f'Here are {len(suggestions)} suggestions:')
                for i in range(len(suggestions)):
                    print(f'{i+1}. {suggestions[i].completed_sentence} ({suggestions[i].source_text} {suggestions[i].offset})')
            else:
                print('There are no suggestions')
            user_input = input(f"{all_user_inputs}")
        if user_input != '*':
            user_input = input("Enter your input:\n")


if __name__ == '__main__':
    main()