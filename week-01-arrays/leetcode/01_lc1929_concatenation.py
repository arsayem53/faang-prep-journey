def concat(numbers):
    temp = numbers.copy()
    for i in range(len(numbers)):
        temp.append(numbers[i])
    return temp

numbers = [10, 40, 70, 80, 30, 60, 50, 20, 90]
numbers = concat(numbers)
for i in range(len(numbers)):
        print(f"{numbers[i]}")