def getConcatenation(nums):
    return nums + nums 
numbers = [10, 40, 70, 80, 30, 60, 50, 20, 90]
ans = getConcatenation(numbers)
print(f"{ans}")


"""
Leetcode version:
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
    """
