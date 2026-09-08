def calculate_average(numbers):
    total = 0

    for num in numbers:
        total += num

    average = total / len(number)

    return average


data = [10, 20, 30, 40, 50]

result = calculate_average(data)

print("Average is: " + result)