"""

Amidakuji is a method of lottery designed to create random pairings between two sets comprised of
an equal number of elements.

Your task is to write a function amidakuji that returns the final positions of each element. Note that
the elements are an ascending sequence of consecutive integers starting with 0 (from left to right).

Input
Your function will receive an array/list of equal-length strings consisting of 0 and 1 characters;
this represents the "ladder" structure. The 1s represent the rungs of the ladder and the 0s represent
empty space.

Each element begins at the top of its corresponding vertical rail, as illustrated in the diagram below.
During the descent of the ladder, whenever a vertical rail intersects a horizontal rung, it swaps values
with the adjacent connecting vertical rail.

Output
Your function should return an array of integers, with each integer in its final position.
"""
from typing import List


def amidakuji(ar: str) -> List[int]:
    numbers = [i for i in range(len(ar[0]) + 1)]

    for num in ar:
        numbers = swapper(num, numbers)

    return numbers


def swapper(num: str, numbers: List[int]) -> List[int]:
    for i in range(len(num)):
        if num[i] == '1':
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

    return numbers