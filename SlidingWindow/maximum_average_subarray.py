# Problem: Maximum Average Subarray I
# Platform: LeetCode
# Difficulty: Easy

class Solution:
    def findMaxAverage(self, nums, k):
        current_sum = sum(nums[:k])
        max_sum = current_sum

        for i in range(k, len(nums)):
            current_sum += nums[i]
            current_sum -= nums[i - k]

            max_sum = max(max_sum, current_sum)

        return max_sum / k
