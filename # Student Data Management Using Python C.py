# Student Data Management Using Python Collections

# Dictionary to store student records
# Key: Roll Number, Value: Tuple(Name, Branch) + List of Marks
students = {}

def add_student(roll_no, name, branch, marks):
    """Add a new student record"""
    if roll_no in students:
        print(f"Student with Roll No {roll_no} already exists!")
    else:
        # Name and Branch stored as a Tuple (immutable),
        # Marks stored as a List (mutable, can be updated)
        students[roll_no] = {
            "details": (name, branch),   # Tuple
            "marks": list(marks)          # List
        }
        print(f"Student {name} (Roll No {roll_no}) added successfully.")

def delete_student(roll_no):
    """Delete an existing student record"""
    if roll_no in students:
        removed = students.pop(roll_no)
        print(f"Student with Roll No {roll_no} ({removed['details'][0]}) deleted successfully.")
    else:
        print(f"Student with Roll No {roll_no} not found!")

def update_student(roll_no, name=None, branch=None, marks=None):
    """Update details of an existing student"""
    if roll_no in students:
        old_name, old_branch = students[roll_no]["details"]
        new_name = name if name else old_name
        new_branch = branch if branch else old_branch
        students[roll_no]["details"] = (new_name, new_branch)  # new Tupleß

        if marks is not None:
            students[roll_no]["marks"] = list(marks)

        print(f"Student with Roll No {roll_no} updated successfully.")
    else:
        print(f"Student with Roll No {roll_no} not found!")

def display_students():
    """Display all student records"""
    print("\n--- Final Student Records ---")
    if not students:
        print("No student records available.")
        return

    for roll_no, info in students.items():
        name, branch = info["details"]
        marks = info["marks"]
        avg_marks = sum(marks) / len(marks) if marks else 0
        print(f"Roll No: {roll_no} | Name: {name} | Branch: {branch} "
              f"| Marks: {marks} | Average: {avg_marks:.2f}")
    print("------------------------------\n")


# ---------------- Main Program ----------------

# Adding student records
add_student(101, "Alice", "CSE", [85, 90, 78])
add_student(102, "Bob", "ECE", [70, 65, 80])
add_student(103, "Charlie", "Mech", [60, 72, 68])

# Display after adding
display_students()

# Updating a student's details (e.g., Bob's branch and marks)
update_student(102, branch="EEE", marks=[75, 80, 85])

# Deleting a student record
delete_student(103)

# Final display after all operations
display_students()