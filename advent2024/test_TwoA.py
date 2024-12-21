from TwoA import is_increasing, is_decreasing

def test_is_increasing():
    assert is_increasing(range(5), 0, 4)
    assert not is_increasing(list(range(5)) + [9], 0, 5)
    assert is_increasing(list(range(5)) + [7], 0, 5)
def test_is_decreasing():
    assert not is_decreasing(range(5), 0, 4)
    assert is_decreasing(list(reversed(range(5))), 0, 4)
    assert is_decreasing(list(reversed(range(5))) + [-2], 0, 5)
    assert not is_decreasing(list(reversed(range(5))) + [-4], 0, 5)

