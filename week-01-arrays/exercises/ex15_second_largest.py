# ex15_second_largest.py
def second_largest_number(arr):
    if len(arr) < 2:
        return None
    largest = arr[0]
    second_largest = None
    for i in range(1, len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > (second_largest if second_largest is not None else float('-inf')) and arr[i] != largest:
            second_largest = arr[i]
    
    return second_largest

arr = [10, 20, 30, 40, 50]
result = second_largest_number(arr)
print(f"Second largest number is: {result}")

