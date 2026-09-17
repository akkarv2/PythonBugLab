a = [1,2,3,4,5,2,3,5,4,1]

repeated = []

for num in a:
    if a.count(num) > 1 and num not in repeated:
        repeated.append(num)

print(repeated) 