from Test.test_predictor import word_dict


# todo change the alg to score to more accurate one ?
def get_score(curr_position, next_position):
    return 2 if curr_position + 1 == next_position else 1


# todo [1] simplify it ? . [2] add explain . [3] more modular so i can make more changes
def update_scores(current_sentences, next_word, total_scores):
    next_sentences = word_dict.get(next_word, {})  # if the word not exist return empty dict6t
    updated_sentences = {}

    for (file, line), positions in current_sentences.items():
        for pos in positions:
            if (file, line) in next_sentences:  # so need to update the score
                for pos_of_next_word in next_sentences[(file, line)]:
                    score = get_score(pos, pos_of_next_word)  # get the score to the completion
                    total_scores[(file, line)] = total_scores.get((file, line), 0) + score  # update the total score
                    updated_sentences.setdefault((file, line), []).append(
                        pos_of_next_word)  # wll return the sentences with the correct index

    # that wll help me to loop over all the sentence with no recursion
    return updated_sentences



def find_sentence(sentence):
    words = sentence.split()
    if not words:
        return []


    current_sentences = {}
    # find the first word that  exist in db
    index_of_first_word = 0
    for idx,word in enumerate(words):
        current_sentences = word_dict.get(word,{})
        if current_sentences != {}:
            index_of_first_word = idx
            break

    total_scores = {}

    for word in words[index_of_first_word:]: # todo its not always 1
        current_sentences = update_scores(current_sentences, word, total_scores)

    # only one word was find
    if total_scores == {}:
        return current_sentences
    return total_scores


sentence = "dont he  want to learn Python today "
print(find_sentence(sentence))
