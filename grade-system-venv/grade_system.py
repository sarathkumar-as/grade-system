# Convert a mark from 0 to 100 into its corresponding letter grade.

def calculate_grade(mark):
    # Return the letter grade for a valid mark.
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def main():
    # Read a mark, validate it, and display the result. #
    user_input = input("Enter your mark (0-100): ").strip()

    try:
        mark = float(user_input)

        if not 0 <= mark <= 100:
            print("Invalid mark. Please enter a number between 0 and 100.")
            return

        grade = calculate_grade(mark)
        print(f"Mark: {mark:g} -> Grade: {grade}")

    except ValueError:
        print("Invalid input. Please enter a number only.")


if __name__ == "__main__":
    main()


