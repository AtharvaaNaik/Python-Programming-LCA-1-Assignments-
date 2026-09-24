# Program to check if a triangle is right-angled using a function

def is_right_angled(a, b, c):
    """
    Checks if the triangle with given sides a, b, c is right-angled.
    Uses the Pythagorean theorem: sum of squares of two smaller sides
    should equal the square of the largest side.
    """
    # Sort sides so that 'largest' is the biggest side
    sides = sorted([a, b, c])
    smallest, middle, largest = sides

    # Check Pythagorean theorem (using round to handle floating point precision)
    if round(smallest**2 + middle**2, 6) == round(largest**2, 6):
        return True
    else:
        return False


# ---------------- Main Program ----------------

# Accepting input from the user
side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))

# First check if it's a valid triangle
if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    if is_right_angled(side1, side2, side3):
        print("The triangle IS a right-angled triangle.")
    else:
        print("The triangle is NOT a right-angled triangle.")
else:
    print("These sides do not form a valid triangle.")