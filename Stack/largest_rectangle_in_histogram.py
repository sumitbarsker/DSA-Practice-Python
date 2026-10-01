# Problem: Largest Rectangle in Histogram
# Platform: LeetCode
# Difficulty: Hard

class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        maximum = 0

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                index, previous_height = stack.pop()

                width = i - index
                maximum = max(maximum, previous_height * width)

                start = index

            stack.append((start, height))

        for index, height in stack:
            width = len(heights) - index
            maximum = max(maximum, height * width)

        return maximum
