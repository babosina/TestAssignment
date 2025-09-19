"""
The function should take two dictionaries as parameters (with default values) and return two tuples:
one containing the matching values and another containing the matching keys.
If one of the dictionaries is not provided, it should be assumed that all values match.
The tuples must be sorted.

def find_dupes('''define'''):
    pass

y = {1: 'a', 4: 'b', 2: 'c', 100: 'e'}
z = {2: 'a', 4: 'b', 9: 'c', 101: 'd'}
assert find_dupes(y, z) == (('a','b','c'), (2, 4))
assert find_dupes(y) == (('a','b','c','e'), (1,2,4,100))
"""


def find_dupes(x: dict = None, y: dict = None) -> tuple:
    x = x or {}
    y = y or {}
    if not x or not y:
        return (tuple(sorted(set(x.values()) | set(y.values()))),
                tuple(sorted(set(x.keys() | set(y.keys())))))

    return (tuple(sorted((set(x.values()) & set(y.values())))),
            tuple(sorted((set(x.keys()) & set(y.keys())))))


def test_find_dupes():
    y = {1: 'a', 4: 'b', 2: 'c', 100: 'e'}
    z = {2: 'a', 4: 'b', 9: 'c', 101: 'd'}

    assert find_dupes(y, z) == (('a', 'b', 'c'), (2, 4))
    assert find_dupes(y) == (('a', 'b', 'c', 'e'), (1, 2, 4, 100))
    assert find_dupes() == ((), ())
