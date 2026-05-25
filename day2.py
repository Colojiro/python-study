def get_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

def get_highest(numbers):
    return max(numbers)

def get_lowest(numbers):
    return min(numbers)

def get_summary(numbers):
    print(f"Average is {get_average(numbers)}")
    print(f"Highest is {get_highest(numbers)}")
    print(f"Lowest is {get_lowest(numbers)}")

grades = [90,98,87,97,88]
test_scores = [70, 65, 80, 95, 60]

get_summary(test_scores)
print("------")
get_summary(grades)






