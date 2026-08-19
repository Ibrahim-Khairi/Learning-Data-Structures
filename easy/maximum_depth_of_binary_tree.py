# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)

# Okay so we just need to see whether the left side of the tree is greater than the right side.
# Every single node is 1 depth, therefore we'll add 1 to our recursive logic, then we just need to take the max of the left side and the right side.
# Our base case would just be the node doesn't exist, in which case we would return 0 and it would stop. We can calculate the left_depth by just calling the root.left on
# left_depth and root.right on the right_depth.