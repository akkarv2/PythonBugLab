def group_numbers(numbers):
    result = {
        "even": [],
        "odd": []
    }

    for number in numbers:
        if number % 2 == 0:
            result["even"].append(number)
        else:
            result["odd"].append(number)

    return result


test_cases = [
    [1, 2, 3, 4, 5, 6],
    [0, -1, -2, 7],
    [],
]

for case in test_cases:
    print(f"Input:  {case}")
    print(f"Output: {group_numbers(case)}")