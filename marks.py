
def calculate_result():
    print("=== Student Marks Calculator ===")

    name = input("Enter student name: ")

    try:
        marks1 = float(input("Enter marks for Subject 1: "))
        marks2 = float(input("Enter marks for Subject 2: "))
        marks3 = float(input("Enter marks for Subject 3: "))

        marks = [marks1, marks2, marks3]

        if any(mark < 0 or mark > 100 for mark in marks):
            print("Error: Marks must be between 0 and 100.")
            return

        total = sum(marks)
        percentage = total / 3

        print("\n--- Student Result ---")
        print("Name:", name)
        print("Total Marks:", total, "/ 300")
        print(f"Percentage: {percentage:.2f}%")

        if all(mark >= 35 for mark in marks):
            print("Result: PASS")
        else:
            print("Result: FAIL")

    except ValueError:
        print("Error: Please enter valid numeric marks.")


if __name__ == "__main__":
    calculate_result()