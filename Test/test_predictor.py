# from predictor import predict_file_line

# Mock data ..

word_occurrences = {
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
    }
}


def predict_file_line(word_occurrences, phrase):
    pass  # need to create


def test_predict_file_line():
    phrase = "I want to"
    predicted_locations = predict_file_line(word_occurrences, phrase)
    assert set(predicted_locations) == {('file1.txt', 3), ('file2.txt', 3)}
