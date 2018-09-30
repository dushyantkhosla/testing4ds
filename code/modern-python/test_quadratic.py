from quadratic import quadratic
from itertools import permutations

def test_quadratic():
    x1, x2 = quadratic(a=8, b=22, c=15)
    assert 8*x1**2 + 22*x1 + 15 == 0
    assert 8*x2**2 + 22*x2 + 15 == 0

def test_quadratic_types():
    x1, x2 = quadratic(a='eight', b=22, c=15)

def test_torture():
    args = [10, 0, -5, 1, -1, 18, 99]
    for t in permutations(args, 3):
        x1, x2 = quadratic(*t)
