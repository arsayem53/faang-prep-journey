# ex10_insert.py
"""
Exercise 9: Insert element at position k
Time Complexity: O(n) - must shift elements
Space Complexity: O(1) - modify in place (or O(n) if creating new array)
"""
def insert_at_position(arr, k, value):
    """Insert value at a index k in the array arr"""
    if k<0 or k>len(arr):
        print("Invalid index")
        return arr
    
    arr.append(0)  
    
    for i in range(len(arr) - 1, k, -1):
        arr[i] = arr[i - 1]
    arr[k] = value
    return arr

arr = [10, 20, 30, 40, 50]
print("Original array:", arr)
target = int(input("Enter the index to insert at (0-5): "))
value = int(input("Enter the value to insert: "))
result = insert_at_position(arr, target, value)
print("Array after insertion:", result)
