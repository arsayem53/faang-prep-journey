# lc1470_shuffle.py
# TODO: Implement
        # Create result array
        # For i from 0 to n-1:
        #   result[2*i] = nums[i]
        #   result[2*i + 1] = nums[i + n]
"""class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [0] * (2 * n)
        for i in range(n):
            result[2 * i] = nums[i]
            result[2 * i + 1] = nums[i + n]
        return result"""

def shuffle(arr, n):
        result = [0] * (2*n)
        for i in range(n):
            result[2*i] = arr[i]
            result[2*i + 1] = arr[i + n]
        return result
arr = [2,5,1,3,4,7]
n = 3
result = shuffle(arr, n)
print(result)  # Output: [2, 3, 5, 4, 1, 7]
        