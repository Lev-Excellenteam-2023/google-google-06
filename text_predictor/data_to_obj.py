import os
from dataclasses import dataclass
from data_extraction.find_text import get_specific_line

@dataclass
class AutoCompleteData:
    completed_sentence: str
    source_text: str
    offset: int
    score: int

def convert_to_autocomplete_data(data_list):

    result = []
    for item in data_list:
        file_data = get_specific_line(item[0][0],item[0][1]).split("\n")[0]
        file_path = os.path.basename(item[0][0]).split(".")[0]
        offset = item[0][1]
        score = item[1]


        autocomplete_data = AutoCompleteData(
            completed_sentence=file_data,
            source_text=file_path,
            offset=offset,
            score=score
        )
        result.append(autocomplete_data)

    return result
