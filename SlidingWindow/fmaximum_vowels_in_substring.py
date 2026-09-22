# Problem: Maximum Number of Vowels in a Substring of Given Length
# Platform: LeetCode
# Difficulty: Medium

class Solution:
    def maxVowels(self, s, k):
        vowels = set("aeiou")

        current = 0

        for char in s[:k]:
            if char in vowels:
                current += 1

        maximum = current

        for i in range(k, len(s)):
            if s[i] in vowels:
                current += 1

            if s[i - k] in vowels:
                current -= 1

            maximum = max(maximum, current)

        return maximum
