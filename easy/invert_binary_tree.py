# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        if root is None:
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

# So we just need to swap the children. We would just return root as is if it's None, that's a given. And to swap, we would just do root.left, root.right = root.right,
# root.left. However, we would call the invert on the terms after the equals to since those would call the invert on both children and assign the swapped results back to
# node.left and node.right. And, at the end we would return the root.
# The subtrees are basically the ones being recursed to actually get back the inverted versions and then we attach them to the current nodes. A more understandable version
# might be:
#     left_inverted = invertTree(node.left)
#     right_inverted = invertTree(node.right)
#
#     node.left = right_inverted
#     node.right = left_inverted
# The one I used is just more compact for simplicity's sake.