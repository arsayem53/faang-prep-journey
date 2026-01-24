# ex11_delete.py
"""
Exercise 10: Delete element at position k
Time Complexity: O(n) - must shift elements
Space Complexity: O(1) - if modifying in place
"""

def delete_at_postion(arr, k):
    if k<0 or k>=len(arr):
        print("Inalid index")
        return arr
    for i in range(k, len(arr) - 1):
        arr[i] = arr[i + 1]
    del arr[-1]
    print(f"Number in {k}th position deleted sucsessfully in !")
    return arr

arr = [10, 20, 30, 40, 50]
print("Original array:", arr)
target = int(input("Enter the index to delete at (0-5): "))
result = delete_at_postion(arr, target)
print("Array after Deleton:", result)