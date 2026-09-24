# Program to validate PAN Number using Regular Expression

import re

def validate_pan(pan):
    """
    Validates PAN number format: AAAAA9999A
    - First 5 characters: uppercase letters (A-Z)
    - Next 4 characters: digits (0-9)
    - Last character: uppercase letter (A-Z)
    """
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    
    if re.match(pattern, pan):
        return True
    else:
        return False


# ---------------- Main Program ----------------

pan_number = input("Enter PAN Number: ")

if validate_pan(pan_number):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")