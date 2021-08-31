"""

Same as the original (same rules, really, go there for example and I
strongly recommend completing it first), but with more than one asterisk (but always at least one).

For example, "*2" should return ["12", "42", "72"].

Similarly, "*2*" should return ["024", "120", "126", "222", "228", "324", "420", "426", "522",
"528", "624", "720", "726", "822", "828", "924"]. Order matters and returning the right one is
part of the challenge itself, yep!

More examples in the test codes and, of course, if you cannot generate any number
divisible by 6, just return [] (or [] of String in Crystal).

"""
from itertools import product
from typing import List


def is_divisible_by_6(string: str) -> List[str]:
    if string[-1] != "*" and int(string[-1]) % 2 == 1:
        return []

    return ["".join(num) for num in product(*list("0123456789" if char == "*"
                                                  else char for char in string))
            if int("".join(num)) % 6 == 0]