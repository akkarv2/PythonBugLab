def find_largest(numbers):
    largest = 0

    for num in numbers:
        if num > largest:
            largest = num

    return largest

data = [12, 45, 8, 99, 23]

result = find_largest(data)

print("Largest number is: " + str(result))