def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]

    for number in numbers:
        if number > largest:
            second = largest
            largest = number
        elif number > second:
            second = number

    return second


test_cases = [
    [10, 5, 8, 20, 15],
    [3, 3, 2, 1],
    [-5, -2, -10, -1],
    [7],
]

for numbers in test_cases:
    print(numbers, "->", second_largest(numbers))