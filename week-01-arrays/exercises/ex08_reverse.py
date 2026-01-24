# ex08_reverse.py
def reverse_array(arr):
    """Reverses the given array in place."""
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [1, 2, 3, 4, 5]
print("Original array:", arr)
print("Reversed array:", reverse_array(arr))