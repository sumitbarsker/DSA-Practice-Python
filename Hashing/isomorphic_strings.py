# Problem: Isomorphic Strings
# Platform: LeetCode
# Difficulty: Easy

class Solution:
    def isIsomorphic(self, s, t):
        mapping_s = {}
        mapping_t = {}

        for a, b in zip(s, t):
            if a in mapping_s and mapping_s[a] != b:
                return False

            if b in mapping_t and mapping_t[b] != a:
                return False

            mapping_s[a] = b
            mapping_t[b] = a

        return True
