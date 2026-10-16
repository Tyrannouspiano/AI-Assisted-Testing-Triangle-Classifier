Part 1
An equilateral triangle can never be a right triangle because all sides of an equilateral triangle are equal. Because of this,
all of the interior angles are equal and as a result, cannot be 90 degrees otherwise it would create a square and not a triangle.

Part 2
Prompted AI to create 5 test cases
Changed the original 5th test which was a degenerate test to be a scalene test.
test_right_scalene_triangle - Copilot suggested - Kept - Creates a right scalene triangle
test_equilateral_triangle - Copilot suggested - Kept - Creates a valid equilateral triangle
test_isosceles_triangle - Copilot suggested - Kept - Creates a valid isosceles triangle
test_invalid_zero_side - Copilot suggested - Kept - Creates an invalid triangle
test_invalid_triangle_inequality - Copilot suggested - Edited to test Scalene triange (2,3,4) - Needed a test for just a scalene triangle
Prompted AI to create 3 more test after realizing degenerate and non-integer cases were not tested - created 2 degenerate tests and a non integer test
test_degenerate_triangle_boundary - Copilot suggested - Kept - creates an invalid degenerate boundary case triangle
test_second_degenerate_triangle_boundary - Copilot suggested - Kept - creates another invalid degenerate boundary case triangle
test_right_isosceles_triangle_with_non_integer_sides - Copilot suggested - Edited - triangle.py originally did not use math and asserted with == instead of isclose. Classify triangle was updated to use math.isclose so that it uses tolerance

