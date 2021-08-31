"""
Write a function filter_long_words that takes a string sentence and an integer n.

Return a list of all words that are longer than n.

Example: filter_long_words("The quick brown fox jumps over the lazy dog", 4) = ['quick', 'brown', 'jumps']

"""
from typing import List


def filter_long_words(sentence: str, n: int) -> List[str]:
    words = []
    words_sentence = sentence.split(" ")

    for word in words_sentence:
        if len(word) > n:
            words.append(word)

    return words