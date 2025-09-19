# Removed the keys passed as a tuple from the dictionary
# Make all changes for the same dictionary


def purge_keys(i_dict: dict, keys: tuple) -> dict:
    """
    Removes keys from a dictionary

    Arguments:
        i_dict {dict} -- dictionary to remove keys from
        keys {tuple} -- keys to remove

    Returns:
        dict -- dictionary with keys removed
    """
    for key in keys:
        if key in i_dict:
            del i_dict[key]
    return i_dict


def test_purge_keys():
    x = {1: 'a', 4: 'b', 2: 'c', 100: 'e'}
    y = {1: 'a', 4: 'b', 2: 'c', 100: 'e'}

    result_1 = purge_keys(x, (1, 2))
    assert result_1 == {4: 'b', 100: 'e'}
    assert result_1 is x

    result_2 = purge_keys(y, ('2', "b"))
    assert result_2 == {1: 'a', 4: 'b', 2: 'c', 100: 'e'}
    assert result_2 is y
