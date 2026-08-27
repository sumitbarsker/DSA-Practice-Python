# Problem: Subsets
# Platform: LeetCode
# Difficulty: Medium

class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(index, current):
            if index == len(nums):
                result.append(current.copy())
                return

            # Include the current number
            current.append(nums[index])
            backtrack(index + 1, current)

            # Don't include the current number
            current.pop()
            backtrack(index + 1, current)

        backtrack(0, [])
        return result
