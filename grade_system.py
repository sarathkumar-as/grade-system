# Convert a mark from 0 to 100 into its corresponding letter grade.

try:
    # Ask the user to enter a mark.
    mark = float(input("Enter your mark (0 to 100): "))

    # Validate the entered mark.
    if mark < 0 or mark > 100:
        print("Error: Please enter a mark between 0 and 100.")

    # Determine the grade.
    elif mark >= 90:
        grade = "A"
        print(f"Your mark is {mark:g} and your grade is {grade}.")

    elif mark >= 80:
        grade = "B"
        print(f"Your mark is {mark:g} and your grade is {grade}.")

    elif mark >= 70:
        grade = "C"
        print(f"Your mark is {mark:g} and your grade is {grade}.")

    elif mark >= 60:
        grade = "D"
        print(f"Your mark is {mark:g} and your grade is {grade}.")

    else:
        grade = "E"
        print(f"Your mark is {mark:g} and your grade is {grade}.")

except ValueError:
    print("Error: Please enter a valid number.")