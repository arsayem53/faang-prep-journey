# ex14_rotate_array.py

def slicing_array(arr,k):
    last_k=arr[-k:]
    first_k=arr[:-k]
    if not arr:
        return arr
    k = k % len(arr)
    return last_k+first_k

arr = [1,2,3,4,5]
k = 6
result = slicing_array(arr, k)
print(arr)  # Output: [1, 2, 3, 4, 5]
print(result)  # Output: [4, 5, 1, 2]

