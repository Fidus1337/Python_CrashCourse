"""
Take random text and try to find out how much times meets any word
"""
from pathlib import Path


def count_words(desired_word: str, path_to_file):

    desired_word = desired_word.lower()

    try:
        file = Path(path_to_file)
        content = file.read_text()
    except FileNotFoundError:
        print("We could not find file, sorry.")
        return None
    words_list = content.split()

    how_much_times_word_meets = 0
    for word in words_list:
        if word.lower() == desired_word:
            how_much_times_word_meets += 1
    return how_much_times_word_meets


print(count_words(
    'she', "Python_Crash_Course/Chapter10_Files&Exceptions/Task_10_10_CommonWords/text.txt")
)
