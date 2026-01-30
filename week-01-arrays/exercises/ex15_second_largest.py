# ex14_second_largest.py
def second_largest_number(arr):
    largest = arr [0]
    second_largest = arr[0]

    for i in range(len(arr)):
        if arr[i] > largest:
           secoond_largest = largest
           largest = arr[i]
        elif arr[i] > second_largest:
           secoond_largest = arr[i]
    return  secoond_largest

arr = [10, 20, 30, 40, 50]
result = second_largest_number(arr)
print(f"Second largest number is: {result}")
