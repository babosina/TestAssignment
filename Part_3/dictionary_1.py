# Create a function that takes a dict and a bool value as input and outputs a sorted array of keys

"""
def get_s_key_val(i_dict, keys=True):
    pass

x = {1: 'a', 4: 'b', 2: 'c', 100: 'e'}

assert get_s_key_val(x, True) == [1,2,4,100]
assert get_s_key_val(x, False) == ['a','b','c','e']
"""


def get_s_key_val(i_dict: dict, keys: bool = True) -> list:
    """
    Return a sorted list of keys

    Args:
        i_dict: Dictionary
        keys: Boolean

    Returns:
        List of keys if keys else List of values
    """
    if not i_dict:
        return []
    if keys:
        return sorted(i_dict.keys())
    return sorted(i_dict.values())


def test_get_s_key_val():
    x = {1: 'a', 4: 'b', 2: 'c', 100: 'e'}

    assert get_s_key_val(x, True) == [1, 2, 4, 100]
    assert get_s_key_val(x, False) == ['a', 'b', 'c', 'e']
    assert get_s_key_val({}) == []
