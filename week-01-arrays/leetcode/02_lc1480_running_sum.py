"""LeetCode #1480: Running Sum of 1d Array
Difficulty: Easy
Link: https://leetcode.com/problems/running-sum-of-1d-array

Problem:
Given an array nums, return an array where result[i] equals the sum of 
nums[0] to nums[i].

Time Complexity: O(n)
Space Complexity: O(1) if modifying in-place, O(n) if creating new array
"""
arr = [10, 40, 70, 80, 30, 60, 50, 20, 90]

for i in range(1, len(arr)  ):
    arr[i] += arr[i-1]
result = arr
print(f"{result}")

"""
Leetcode version:
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
    """