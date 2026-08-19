# okay im doing path sum
# i wrote it out entirely
# path_sum += root.val
# path_sum += root.left.val
# path_sum += root.right.val
# path_sum += root.left.left.val
# path_sum += root.left.right.val
# path_sum += root.right.left.val
# path_sum += root.right.right.val
#
# path_sum += root.left.left.left.val
# path_sum += root.left.left.right.val
# path_sum += root.left.right.left.val
# path_sum += root.left.right.right.val
# path_sum += root.right.left.left.val
# path_sum += root.right.left.right.val
# path_sum += root.right.right.left.val
# path_sum += root.right.right.right.val

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        if root is None:
            return False

        remaining = targetSum - root.val

        if remaining == 0 and root.left is None and root.right is None:
            return True
        else:
            return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)

# Tree version of Two Sum, LMAO. Except, there's no two pointers and stuff. We actually follow the remaining approach.
# If root is None, that would automatically mean there's nothing to compare targetSum with, therefore that automatically returns False.
# Then we would derive remaining with targetSum - root.val, this would happen recursively.
# The problem specifically asks for "to-leaf", which means that our recursion would only end when our current node (root) doesn't have any children, for which we would check
# both the root.left and root.right being None. The targetSum comparison would be equal if there's nothing remaining precisely, and it not being either in positive (we
# haven't met the targetSum) or negative (it exceeded targetSum).
# Otherwise, if any of the children exist, we'll call the recursion on both the lefts and right sides, with remaining replacing targetSum since that's basically our new
# target.