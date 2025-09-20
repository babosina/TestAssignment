# Make a function that receives a dict of dictionaries as an input and invert inner dictionaries.
# Passed dict should remain untouched

def invert_inner_dicts(i_dict: dict) -> dict:
    """
    Inverts inner dictionaries.

    Arguments:
        i_dict {dict} -- Inner dictionary to invert.

    Returns:
        dict -- Inverted inner dictionaries.
    """
    new_dict = {}
    for key, value in i_dict.items():
        new_dict[key] = {v: k for k, v in value.items()}
    return new_dict


def test_invert_inner_dicts():
    p1 = {'a': 1}
    p2 = {'b': 2, 'e': 8}
    task_d = {'f': p1, 'df': p2}

    i_result = invert_inner_dicts(task_d)
    assert i_result == {'f': {1: 'a'}, 'df': {2: 'b', 8: 'e'}}
    assert task_d == {'f': {'a': 1}, 'df': {'b': 2, 'e': 8}}
