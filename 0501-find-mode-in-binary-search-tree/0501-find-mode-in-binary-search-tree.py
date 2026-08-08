# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        result = []
        stack = []
        curr = root
        prev = None
        count = 0
        max_count = 0

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if curr.val == prev:
                count += 1
            else:
                count = 1

            if count > max_count:
                max_count = count
                result = [curr.val]
            elif count == max_count:
                result.append(curr.val)

            prev = curr.val
            curr = curr.right

        return result