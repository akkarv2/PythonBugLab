def reverse_list(data):
    left = 0
    right = len(data)

    while left < right:
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1

    return