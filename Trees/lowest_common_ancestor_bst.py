# Problem: Lowest Common Ancestor of a Binary Search Tree
# Platform: LeetCode
# Difficulty: Medium

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        current = root

        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left

            elif p.val > current.val and q.val > current.val:
                current = current.right

            else:
                return current
