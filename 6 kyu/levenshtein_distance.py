"""
In information theory and computer science, the Levenshtein distance is a string
metric for measuring the difference between two sequences. Informally, the Levenshtein
distance between two words is the minimum number of single-character edits (i.e. insertions,
deletions or substitutions) required to change one word into the other.
"""
def levenshtein(a: str, b: str) -> int:
    if not a:
        return len(b)
    elif not b:
        return len(a)
    elif a[0] == b[0]:
        return levenshtein(a[1:], b[1:])
    else:
        return 1 + min(levenshtein(a[1:], b),
                       levenshtein(a, b[1:]),
                       levenshtein(a[1:], b[1:]))