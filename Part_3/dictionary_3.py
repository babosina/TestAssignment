# Return a value by a key. If there is no key - return the key itself
# Provide at least 2 solutions

def get_val(i_dict: dict, key=None):
    """
    Returns the value of a key from the dictionary

    Arguments:
        dictionary {dict} -- The dictionary to look up
        key {str} -- The key to look up

    Returns:
        The value of the Key from the dictionary
        If there is no key, returns Key
    """
    return i_dict.get(key) if key in i_dict else key


def get_value(i_dict: dict, key=None):
    return i_dict.get(key, key)


def test_get_val():
    x = {1: 'a', 4: 'b', 2: 'c', 100: 'e'}

    assert get_val(x, 1) == 'a'
    assert get_val(x, 500) == 500


def test_get_value():
    x = {1: 'a', 4: 'b', 2: 'c', 100: 'e'}

    assert get_val(x, 1) == 'a'
    assert get_val(x, 500) == 500
