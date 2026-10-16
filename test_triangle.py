from math import sqrt

from triangle import classify_triangle

def test_right_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "right Scalene"


def test_equilateral_triangle():
    assert classify_triangle(5, 5, 5) == "Equilateral"


def test_isosceles_triangle():
    assert classify_triangle(2, 2, 3) == "Isosceles"


def test_invalid_zero_side():
    assert classify_triangle(0, 1, 1) == "Invalid"


def test_scalene_triangle():
    assert classify_triangle(2, 3, 4) == "Scalene"


def test_degenerate_triangle_boundary():
    assert classify_triangle(1, 2, 3) == "Invalid"


def test_second_degenerate_triangle_boundary():
    assert classify_triangle(2, 3, 5) == "Invalid"


def test_right_isosceles_triangle_with_non_integer_sides():
    assert classify_triangle(5, 5, 5 * sqrt(2)) == "right Isosceles"
