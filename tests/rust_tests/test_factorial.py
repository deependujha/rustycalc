import pytest
import rustycalc as rc

@pytest.mark.parametrize(
    "a,b",
    [
        (0,1),
        (1,1),
        (2,2),
        (3,6),
        (4,24),
        (5,120),
        (6,720),
        (7,5040),
        (8,40320)
    ],
)
def test_factorial(a,b):
    assert rc.factorial(a) == b