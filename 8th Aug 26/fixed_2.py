def get_even_numbers(numbers):
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers


data = [10, 15, 20, 25, 30, 35, 40]

result = get_even_numbers(data)

print(f"Even numbers are: {result}")

print(f"Total even number: {len(result)}")