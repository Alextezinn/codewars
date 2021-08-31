"""
To complete this Kata you need to make a function multiplyAll/multiply_all which takes an array
of integers as an argument. This function must return another function, which takes a single integer
as an argument and returns a new array.

The returned array should consist of each of the elements from the first array multiplied by the integer.

Example: multiply_all([1, 2, 3])(2); // => [2, 4, 6]

You must not mutate the original array.

"""

from typing import List


def multiply_all(list_num: List[int]) -> List[int]:
    def new_list_num(mult: int) -> List[int]:
        if not list_num:
            return []
        return [num * mult for num in list_num]
    return new_list_num