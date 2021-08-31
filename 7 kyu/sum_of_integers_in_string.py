"""
Your task in this kata is to implement a function that calculates the sum of the integers inside a string.

For example, in the string "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", the sum of the
integers is 3635.
"""
def sum_of_integers_in_string(string: str) -> int:
    total, current = 0, ""

    for char in string:
        if char.isdigit():
            current = "".join([current, char])
        elif current != "":
            total += int(current)
            current = ""

    if current.isdigit():
        total += int(current)

    return total