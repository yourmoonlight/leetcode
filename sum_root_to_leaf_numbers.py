# definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.sum(root, 0)

    def sum(self, root, presum):
        if root is None:
            return 0
        presum = presum * 10 + root.val
        if root.left is None and root.right is None:
            return presum
        return self.sum(root.left, presum) + self.sum(root.right, presum)
