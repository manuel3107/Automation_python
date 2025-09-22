import pytest
from calculadora import suma, resta, multiplicacion, division

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15),
    (-6, 3, -3),
    (2, 4, 6),
])
def test_suma(a, b, expected):
    assert suma(a, b) == expected

def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)