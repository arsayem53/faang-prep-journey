# lc1365_smaller_numbers.py
def smaller_number(arr):
    count = [0] * len(arr)
    for i in range(len(arr)):
        nums = 0
        for j in range(len(arr)):
            if arr[i] > arr[j]:
               nums += 1
        count[i] = nums
    return count
arr = [8,1,2,2,3]
result = smaller_number(arr)
print(f"Count of smaller numbers: {result}")


"""class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        for i in range(len(nums)):
            nums_count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                   nums_count += 1
            count[i] = nums_count
        return count"""