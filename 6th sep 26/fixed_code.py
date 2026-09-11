def find_largest_even(numbers):
    largest = None

    for num in numbers:
        if num % 2 == 0:
            if largest == None:
                largest = num
            elif num > largest:
                largest = num

    return largest

data = [7, 12, 5, 20, 3, 18, 25]

result = find_largest_even(data)

print("Largest even number is: " + str(result))