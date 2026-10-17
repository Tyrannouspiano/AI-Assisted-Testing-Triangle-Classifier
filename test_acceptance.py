from math import sqrt
from triangle import classify_triangle


def test_acceptance():
    assert classify_triangle(3, 3, 3) == "Equilateral"
    assert classify_triangle(3, 3, 4) == "Isosceles"
    assert classify_triangle(2, 3, 4) == "Scalene"
    assert classify_triangle (0, 1, 0) == "Invalid"
    assert classify_triangle (-1, 2, 2) == "Invalid"
    assert classify_triangle(3, 4, 5) == "right Scalene"
    assert classify_triangle(5, 5, 5 * sqrt(2)) == "right Isosceles"