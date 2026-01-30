# ex17_is_sorted.py
def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
           return False
    return True
arr = [10, 20, 30, 40, 0]
result = is_sorted(arr)
print(f"Array is sorted: {result}")
