
def add_student(students, name, grade):
    """
    Add a new student.
    Validate: grade 0-100, name not empty.
    """
    if name.strip() == "":
        print("Name cannot be empty.")
        return
    if grade < 0 or grade > 100:
        print("Grade must be between 0 and 100.")
        return
    new_student = {"name": name, "grade": grade}
    students.append(new_student)
    print("Student added successfully.")

def remove_student(students, index):
    """
    Remove student at given index.
    Validate: index is valid, list not empty.
    """
    if len(students) == 0:
        print("No students to remove.")
        return

    if index < 0 or index >= len(students):
        print("Invalid index.")
        return
    students.pop(index)
    print("Student removed successfully.")

def show_all(students):
    """
    Display all students with index.
    Format: [index] Name - Grade
    """
    # TODO: Implement
    if len(students) == 0:
        print("No students found.")
        return

    for index, student in enumerate(students):
        print(f"[{index}] {student['name']} - {student['grade']}")

def calculate_average(students):
    """
    Calculate average of all grades.
    Return: float average, or None if empty.
    """
    if len(students) == 0:
        return None
    total = 0
    for student in students:
        total += student["grade"]
    average = total / len(students)
    return average
    

def find_highest(students):
    if len(students) == 0:
        return None

    highest_student = students[0]

    for student in students:
        if student["grade"] > highest_student["grade"]:
            highest_student = student

    return highest_student

def find_lowest(students):
    """
    Find student with lowest grade.
    Return: the student dict, or None if empty.
    """
    if len(students) == 0:
        return None

    lowest_student = students[0]

    for student in students:
        if student["grade"] < lowest_student["grade"]:
            lowest_student = student

    return lowest_student

def count_above_average(students):
    """
    Count students with grade above average.
    Return: count (int), or None if empty.
    """
    if len(students) == 0:
        return None
    average = calculate_average(students)
    above_student = 0
    for student in students:
        if student["grade"] > average:
            above_student += 1

    return above_student

def show_sorted(students):
    """
    Display students sorted by grade (high to low).
    DON'T modify the original list — sort a copy!
    """
    if len(students) == 0:
        print("No students found.")
        return  
    new_students = students.copy()
    sorted_students = sorted(new_students, key=lambda x: x["grade"], reverse=True)
    for index, student in enumerate(sorted_students):
        print(f"[{index}] {student['name']} - {student['grade']}")
    

def show_menu():
    """Print the main menu."""
    print("\n=============================================")
    print("    🎓 Student Grade Manager")
    print("=============================================")
    print("1. Add a student")
    print("2. Remove student by index")
    print("3. Show all students")
    print("4. Calculate average")
    print("5. Find highest grade")
    print("6. Find lowest grade")
    print("7. Count grades above average")
    print("8. Show grades sorted")
    print("9. Exit")
    print("=============================================")

students = []
while True:
        show_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            name = input("Enter student name: ")
            try:
               grade = int(input("Enter grade (0-100): "))
            except ValueError:
               print("Enter a valid number for grade.")
               continue
            add_student(students, name, grade)


        elif choice == "2":
            show_all(students)
            try:
               index = int(input("Enter index to remove: "))
            except ValueError:
                print("Enter a valid index.")
                continue
            remove_student(students, index)

        elif choice == "3":
            show_all(students)

        elif choice == "4":
            result = calculate_average(students)

            if result is None:
               print("No students to calculate average.")
            else:
               print(f"Average result is {result:.2f}")


        elif choice == "5":
            highest = find_highest(students)
            if highest is None:
                print("No students to calculate Highest.")
            else:
               print(f"Highest result is {highest}")
               
        elif choice == "6":
            # TODO: Call find_lowest, print result
            lowest = find_lowest(students)
            if lowest is None:
                print("No students to calculate Lowest.")
            else:
               print(f"Lowest result is {lowest}")

        elif choice == "7":
            # TODO: Call count_above_average, print result
            above = count_above_average(students)
            if above is None:
                print("No students to calculate above average.")
            else:
               print(f"There are {above} students who are above average")

        elif choice == "8":
            show_sorted(students)

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Enter 1-9.")
