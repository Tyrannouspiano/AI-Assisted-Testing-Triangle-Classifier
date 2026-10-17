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

Part 4
Tests are run by sunning the command python -m pytest test_triangle.py -v to run the test_triangle test, 
python -m pytest test_acceptance.py -v to test the test_acceptance test, or python -m pytest -v to run and see all the tests
Equivalence classes identified based on triangle classifications are equilateral, isosceles, scalene, right isosceles, right scalene, and invalid if there is a 0 for a side, negative for a side, or if the side lengths do not form a proper triangle.
Boundary values indentified are sides length must be greater than zero, two added sides must be greater than the third, if all sides are equal an triangle is equilateral, if only 2 sides are equal, the triangle is isosceles, and if the pythagoreon theorem is true the triangle is a right triangle (uses math.isclose to account for floating point rounding so there is tolerance)

AI DISCLOSURE
AI was used to help create both functions in triangle.py (is_valid_triangle and classify_triangle). Classify triangle was edited to use math.isclose so there is tolerance for floating point values. VSCode's Copilot was also used to draft tests in test_triangle.py. These were reviewed to make sure they met all the necessary criteria and one was edited so that all possible triangles were created and invalid combinations returned invalid. Finally, ChatGPT was used to clarify equivalence classses and boundaries because I wasn't 100% sure what it wanted there.