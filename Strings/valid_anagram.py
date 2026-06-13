# Problem: Valid Anagram
# Platform: LeetCode
# Difficulty: Easy

class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
