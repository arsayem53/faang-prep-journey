# ex11_remove_duplicates.py

def remove_duplicates(arr):
    """remove_duplicates(arr) takes an array and returns a new array with duplicates removed."""
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

arr = [1, 2, 2, 3, 4, 4, 5]
print(f"Original array: {arr}")
print(f"Array without duplicates: {remove_duplicates(arr)}")