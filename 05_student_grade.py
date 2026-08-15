# Student Grade Calculator

def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


name = input("Enter student name: ")

mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))

average = (mark1 + mark2 + mark3) / 3
grade = calculate_grade(average)

print("\n--- Student Result ---")
print("Student:", name)
print("Average:", round(average, 2))
print("Grade:", grade)