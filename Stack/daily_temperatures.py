# Problem: Daily Temperatures
# Platform: LeetCode
# Difficulty: Medium

class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                previous = stack.pop()
                result[previous] = i - previous

            stack.append(i)

        return result
