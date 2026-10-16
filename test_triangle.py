from triangle import classify_triangle


def test_right_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "right Scalene"


def test_equilateral_triangle():
    assert classify_triangle(5, 5, 5) == "Equilateral"


def test_isosceles_triangle():
    assert classify_triangle(2, 2, 3) == "Isosceles"


def test_invalid_zero_side():
    assert classify_triangle(0, 1, 1) == "Invalid"


def test_invalid_triangle_inequality():
    assert classify_triangle(1, 2, 3) == "Invalid"
