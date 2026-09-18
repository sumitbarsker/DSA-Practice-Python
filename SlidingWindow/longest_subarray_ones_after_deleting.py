# Problem: Longest Subarray of 1's After Deleting One Element
# Platform: LeetCode
# Difficulty: Medium

class Solution:
    def longestSubarray(self, nums):
        left = 0
        zeros = 0
        longest = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1

                left += 1

            longest = max(longest, right - left)

        return longest
