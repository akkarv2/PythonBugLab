def reverse_list(data):
    left = 0
    right = len(data)-1

    while left < right:
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1

    return data
print(reverse_list([1,2,3,4,5]))