# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if root is None:
            return 0
        if root.left is None:
            return 1 + self.minDepth(root.right)
        if root.right is None:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

# This one's slightly different than Maximum Depth because we need to think about what if one of the children is null. In that case, we would just call the recursion on the
# other child. This would only happen if one of the children is null. In the case that we have reached a post-leaf node and root happens to be None, we'll end the recursion.
# On every recursive case, we'll call 1 to add the depth, and if both the children exist, then we'll just take the min of both depths.