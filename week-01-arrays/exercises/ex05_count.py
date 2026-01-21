#ex05_count.py

def arr_count(numbers):
    total = 0
    target = int(input("Enter your target number: "))
    for num in numbers:
        if target == num:
            total += 1
        else:
            continue
    return total


numbers = [10, 40, 20, 80, 30, 60, 20, 20, 90]

count = arr_count(numbers)
print(f"Occurence = {count}")
