# Problem: Find All Anagrams in a String
# Platform: LeetCode
# Difficulty: Medium

class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        count_p = [0] * 26
        count_s = [0] * 26
        result = []

        for char in p:
            count_p[ord(char) - ord('a')] += 1

        for i in range(len(s)):
            count_s[ord(s[i]) - ord('a')] += 1

            if i >= len(p):
                count_s[ord(s[i - len(p)]) - ord('a')] -= 1

            if count_s == count_p:
                result.append(i - len(p) + 1)

        return result
