# from predictor import predict_file_line

# Mock data ..

word_dict = {
    'I': {
        ('file1.txt', 3): [0],
        ('file2.txt', 3): [0],
        ('file3.txt', 2): [0]
    },
    'want': {
        ('file1.txt', 3): [1],
        ('file2.txt', 3): [1],
        ('file3.txt', 2): [2]
    },
    'to': {
        ('file1.txt', 3): [2],
        ('file2.txt', 3): [2],
        ('file3.txt', 2): [3]
    },
    'learn': {
        ('file1.txt', 3): [3]
    },
    'go': {
        ('file2.txt', 3): [3]
    },
    'home.': {
        ('file2.txt', 3): [4]
    },
    "don't": {
        ('file3.txt', 2): [1]
    },
    'stay.': {
        ('file3.txt', 2): [4]
    },
    'Python': {
        ('file1.txt', 3): [4],
    },
    'The': {
        ('file1.txt', 1): [0]
    },
    'sun': {
        ('file1.txt', 1): [1]
    },
    'is': {
        ('file1.txt', 1): [2],
        ('file2.txt', 2): [1],
        ('file2.txt', 4): [2],
        ('file3.txt', 3): [1]
    },
    'shining.': {
        ('file1.txt', 1): [3]
    },
    'Birds': {
        ('file1.txt', 2): [0]
    },
    'chirp': {
        ('file1.txt', 2): [1]
    },
    'in': {
        ('file1.txt', 2): [2],
        ('file3.txt', 1): [2]
    },
    'the': {
        ('file1.txt', 2): [3]
    },
    'morning.': {
        ('file1.txt', 2): [4]
    },
    'Rainbows': {
        ('file1.txt', 4): [0]
    },
    'appear': {
        ('file1.txt', 4): [1]
    },
    'after': {
        ('file1.txt', 4): [2]
    },
    'rain.': {
        ('file1.txt', 4): [3]
    },
    'Never': {
        ('file2.txt', 1): [0]
    },
    'stop': {
        ('file2.txt', 1): [1]
    },
    'asking': {
        ('file2.txt', 1): [2]
    },
    'questions.': {
        ('file2.txt', 1): [3]
    },
    'Knowledge': {
        ('file2.txt', 2): [0]
    },
    'essential.': {
        ('file2.txt', 2): [2]
    },

    'universe': {
        ('file2.txt', 4): [1]
    },
    'vast.': {
        ('file2.txt', 4): [3]
    },
    'Flowers': {
        ('file3.txt', 1): [0]
    },
    'bloom': {
        ('file3.txt', 1): [1]
    },
    'spring.': {
        ('file3.txt', 1): [3]
    },
    'Winter': {
        ('file3.txt', 3): [0]
    },
    'cold': {
        ('file3.txt', 3): [2]
    },
    'and': {
        ('file3.txt', 3): [3]
    },
    'crisp.': {
        ('file3.txt', 3): [4]
    },
    'Nature': {
        ('file3.txt', 4): [0]
    },

    'truly': {
        ('file3.txt', 4): [2]
    },
    'wonderful.': {
        ('file3.txt', 4): [3]
    }
}




def predict_file_line(word_occurrences, phrase):
    pass  # need to create


def test_predict_file_line():
    phrase = "I want to"
    predicted_locations = predict_file_line(word_dict, phrase)
    assert set(predicted_locations) == {('file1.txt', 3), ('file2.txt', 3)}
