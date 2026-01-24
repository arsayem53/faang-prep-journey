# lc1672_richest_customer.py
"""
LeetCode #1672: Richest Customer Wealth
Difficulty: Easy
Link: https://leetcode.com/problems/richest-customer-wealth

Problem:
Given m x n matrix accounts where accounts[i][j] is the amount of money
the i-th customer has in the j-th bank, return the wealth of the richest customer.

Time Complexity: O(m × n) - m rows, n columns
Space Complexity: O(1)
"""
accounts = [[1, 2, 3], [4, 2, 1]]
max_wealth = 0
for customer in accounts:
    wealth = sum(customer)
    max_wealth = max(max_wealth, wealth)
print(f"The richest customer has wealth: {max_wealth}")
"""
Leetcode version:
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            wealth = sum(customer)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth"""