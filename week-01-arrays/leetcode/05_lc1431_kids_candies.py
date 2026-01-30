"""# lc1431_kids_candies.py
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_number = max(candies)
        condition = [0]*len(candies)
        for i in range(len(candies)):
            current_val=candies[i]+extraCandies
            if current_val >= max_number:
               condition[i] = True
            else:
               condition[i] = False
        return condition
    """
def kidsWithCandies(candies, extraCandies):
    max_number = max(candies)
    condition = [0] * len(candies)
    for i in range(len(candies)):
        current_val = candies[i] + extraCandies
        if current_val >= max_number:
            condition[i] = True
        else:
            condition[i] = False
    return condition
candies = [2, 3, 5, 1, 3]
extraCandies = 3
result = kidsWithCandies(candies, extraCandies)
print(result)  # Output: [True, True, True, False, True]
