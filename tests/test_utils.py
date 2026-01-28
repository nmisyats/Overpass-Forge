from overpassforge._utils import partition

def test_partition():
    t, f = partition(lambda a: a % 2 == 0, [1, 2, 3, 4, 5, 6])
    assert t == [2, 4, 6]
    assert f == [1, 3, 5]
