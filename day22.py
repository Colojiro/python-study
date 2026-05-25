
def get_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

grades = [90,98,87,97,70]

for grade in grades:
    if grade >= 90:
        print(f"{grade} - Excellent")
    elif grade >=80:
        print(f"{grade} - Good")
    else:
        print(f"{grade} - Needs improvement")

print("")

students = [
    {"name": "Juan", "grade": 90, "scores": [90,98,87]},
    {"name": "Maria", "grade": 75, "scores": [75,80,70]},
    {"name": "Jose", "grade": 85, "scores": [85,88,92]}
]

for student in students:
    avg = get_average(student["scores"])
    if avg >= 90:
        print(f"{student['name']} Average: {avg:.2f} - Excellent")
    elif avg >= 80:
        print(f"{student['name']} Average: {avg:.2f} - Good")
    else:
        print(f"{student['name']} Average: {avg:.2f} - Needs Improvement")



