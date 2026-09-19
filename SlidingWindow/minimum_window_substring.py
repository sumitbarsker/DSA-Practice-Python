# Problem: Minimum Window Substring
# Platform: LeetCode
# Difficulty: Hard

class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        count_t = {}

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        left = 0
        required = len(t)
        min_length = float("inf")
        start = 0

        for right in range(len(s)):
            char = s[right]

            if char in count_t:
                if count_t[char] > 0:
                    required -= 1

                count_t[char] -= 1

            while required == 0:
                window_length = right - left + 1

                if window_length < min_length:
                    min_length = window_length
                    start = left

                left_char = s[left]

                if left_char in count_t:
                    count_t[left_char] += 1

                    if count_t[left_char] > 0:
                        required += 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[start:start + min_length]
