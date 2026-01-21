#ex06_linear_search.py

def arr_linear_search(numbers):
    position = -1
    target = int(input("Enter your target number: "))
    for i in range(len(numbers)):
        if target == numbers[i]:
            position = i
            break
        else:
            continue
    return position


numbers = [10, 40, 20, 80, 30, 60, 20, 20, 90]

position = arr_linear_search(numbers)
if position == -1:
    print(f"Not found")
else:
    print(f"Position = {position}")
