# Student Grade System – Learning Notes

## 1. User Input

The `input()` function collects a value entered by the user.

```python
mark = float(input("Enter your mark (0 to 100): "))
```

`input()` initially returns text. The `float()` function converts that text into a number.

## 2. Conditional Statements

The program uses `if`, `elif`, and `else` to compare the mark with the grading boundaries.

```python
if mark >= 90:
    grade = "A"
elif mark >= 80:
    grade = "B"
```

Python checks the conditions from top to bottom. Therefore, the highest grade condition must appear first.

## 3. Input Validation

The program checks whether the entered mark is between 0 and 100.

```python
if mark < 0 or mark > 100:
    print("Error: Please enter a mark between 0 and 100.")
```

This prevents invalid values such as `-5` and `105` from receiving a grade.

## 4. Error Handling

The `try` and `except` blocks prevent the program from crashing when the user enters text instead of a number.

```python
try:
    mark = float(input("Enter your mark: "))
except ValueError:
    print("Error: Please enter a valid number.")
```

## 5. Formatted Output

An f-string combines variables and text in a readable output message.

```python
print(f"Your mark is {mark:g} and your grade is {grade}.")
```

## 6. Test Results

| Test Input | Expected Result | Status |
| ---------: | --------------- | ------ |
|         95 | Grade A         | Passed |
|         85 | Grade B         | Passed |
|         75 | Grade C         | Passed |
|         65 | Grade D         | Passed |
|         50 | Grade E         | Passed |
|         -1 | Error message   | Passed |
|        101 | Error message   | Passed |
|        abc | Error message   | Passed |

## Conclusion

This assignment helped me understand Python input, numerical conversion, conditional statements, validation, exception handling, and formatted output. It also introduced me to organising and publishing a coding project with Git and GitHub.
