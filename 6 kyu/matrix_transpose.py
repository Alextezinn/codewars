"""

Write a function that outputs the transpose of a matrix - a new matrix where
the columns and rows of the original are swapped.

"""
from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]