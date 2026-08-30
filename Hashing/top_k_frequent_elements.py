# Problem: Top K Frequent Elements
# Platform: LeetCode
# Difficulty: Medium

from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)

        return [num for num, frequency in count.most_common(k)]
