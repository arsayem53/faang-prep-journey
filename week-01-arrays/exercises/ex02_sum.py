#ex02_sum.py

def arr_sum(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total


numbers = [10, 40, 70, 80, 30, 60, 50, 20, 90]

total = arr_sum(numbers)
print(f"Array sum is: {total}")