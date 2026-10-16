import math

#This funtion takes the input for 3 sides of the triangle and returns if the triangle is valid or not by checking if any side
#has a length equal to zero or if any two sides add up to less than or equal to the third
def is_valid_triangle (a,b,c) -> bool:
    if a <= 0 or b <= 0 or c<= 0:
            return False
    if a + b <= c or a + c <= b or b + c <= a:
          return False

    return True


##This function takes the sides of the triangle and checks if it a valid triangle
#If it isn't valid, it returns "Invalid"
#If it is valid it returns the type of triangle is it if calculates what type of triangle it is (Equilateral, Scalene, Isosceles)
#Finally, it checks if it stisfies the Pythagorean theorem and prefixies the result with "right" if the triangle is a right triangle

def classify_triangle (a,b,c) -> str:
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or a == c or b == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    sides = sorted([a, b, c])
    if math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2):
        return "right " + triangle_type 
    #Changed from return f"right {triangle_type}" to return "right " + triangle_type (more comfortable with latter)
    #Edited to use math.isclose so noninteger values work (5,5, 5*sqrt(2))
    
    return triangle_type