from Test.test_predictor import word_dict


def find_sentence_locations(word_dict, sentence):
    words = sentence.split()

    if len(words) == 1 and words[0] in word_dict:
        return list(word_dict[words[0]].keys())

    start_points = word_dict.get(words[0], {})
    matched_locations = []

    for file_line, indices in start_points.items():
        for index in indices:
            if all(word in word_dict and file_line in word_dict[word] and index + i in word_dict[word][file_line]
                   for i, word in enumerate(words[1:], 1)):
                matched_locations.append(file_line)

    return matched_locations


def replace_score(position: int) -> int:
    scores = [-5, -4, -3, -2]
    return scores[position] if position < len(scores) else -1


def add_or_delete_score(position: int) -> int:
    scores = [-10, -8, -6, -4]
    return scores[position] if position < len(scores) else -2


def generate_sentences(sentence):
    results = []
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(len(sentence)):
        if sentence[i] != " ":
            # Replace characters
            for char in alphabets:
                if sentence[i] != char:
                    new_sentence = sentence[:i] + char + sentence[i + 1:]
                    score = replace_score(i)
                    results.append((new_sentence, score))
            # Delete characters
            new_sentence = sentence[:i] + sentence[i + 1:]
            score = add_or_delete_score(i)
            results.append((new_sentence, score))

    for i in range(len(sentence) + 1):
        if i == len(sentence) or sentence[i] != " ":
            for char in alphabets:
                new_sentence = sentence[:i] + char + sentence[i:]
                score = add_or_delete_score(i)
                results.append((new_sentence, score))
    # print(results)
    # results = results.remove(sentence)
    return results


def get_sentences_and_scores(input_sentence, word_dict):
    input_len = len(input_sentence.replace(" ", ""))
    found_sentences = find_sentence_locations(word_dict, input_sentence)

    result = [(s, 2 * input_len) for s in found_sentences]

    added_sentences = {s[0] for s in result}

    if len(result) < 5:
        generated_sentences_with_scores = generate_sentences(input_sentence)
        generated_sentences_with_scores.sort(key=lambda x: x[1])

        for sentence, gen_score in generated_sentences_with_scores:
            found_for_generated = find_sentence_locations(word_dict, sentence)

            for s in found_for_generated:
                if s not in added_sentences:
                    if len(result) < 5:
                        score = 2 * input_len + gen_score
                        result.append((s, score))
                        added_sentences.add(s)
                    else:
                        break
            if len(result) == 5:
                break

    return result



if __name__ == '__main__':
    original_sentence = "I want"
    print(get_sentences_and_scores(original_sentence,word_dict))