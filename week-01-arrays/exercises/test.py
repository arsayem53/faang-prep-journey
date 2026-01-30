def slicing_array(arr,k):
    last_k=arr[-k:]
    first_k=arr[:-k]
    return last_k+first_k

arr = [1,2,3,4,5]
k = 2
result = slicing_array(arr, k)
print(arr)  # Output: [1, 2, 3, 4, 5]
print(result)  # Output: [4, 5, 1, 2]
