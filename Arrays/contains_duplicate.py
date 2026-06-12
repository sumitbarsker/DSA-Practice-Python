# Problem: Contains Duplicate
# Platform: LeetCode
# Difficulty: Easy

class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
