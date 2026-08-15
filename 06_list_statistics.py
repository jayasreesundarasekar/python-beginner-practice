# List Statistics Program

def calculate_statistics(numbers):
    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)

    return total, average


numbers = [10, 20, 30, 40, 50]

total, average = calculate_statistics(numbers)

print("Numbers:", numbers)
print("Total:", total)
print("Average:", average)
print("Highest:", max(numbers))
print("Lowest:", min(numbers))