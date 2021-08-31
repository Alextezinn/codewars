"""

Task:
The function that you have to write accepts two list/array, xxx and yyy, representing the
coordinates of the points to regress (so that, for example, the first point has coordinates (x[0], y[0])).

Your function should return a tuple (in Python) or an array (any other language) of two
elements: a (intercept) and b (slope) in this order.

You must round your result to the first 4 decimal digits
"""
from typing import List, Tuple


def regressionLine(x: List[int], y: List[int]) -> Tuple[float, float]:
    n = len(x)
    sum_x_square = sum(xi ** 2 for xi in x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_product_x_y = sum(xi * yi for xi, yi in zip(x, y))
    denominator = n * sum_x_square - sum_x ** 2

    a = round((sum_x_square * sum_y - sum_x * sum_product_x_y) / denominator, 4)
    b = round((n * sum_product_x_y - sum_x * sum_y) / denominator, 4)

    return a, b