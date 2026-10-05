def calculate_result(marks):
    if not marks:
        raise ValueError("Marks cannot be empty")

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100")

    total = sum(marks)
    percentage = total / len(marks)

    result = "PASS" if all(mark >= 35 for mark in marks) else "FAIL"

    return total, percentage, result