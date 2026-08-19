# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root, left_base=None, right_base=None):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is not None:
            left_base = root.left
            right_base = root.right

        if left_base is None and right_base is None:
            return True
        if left_base is None or right_base is None:
            return False

        values_match = left_base.val == right_base.val
        outer_match = self.isSymmetric(None, left_base.left, right_base.right)
        inner_match = self.isSymmetric(None, left_base.right, right_base.left)

        return values_match and outer_match and inner_match

# This essentially follows the same fundamentals as same_tree does, however it has to be mirrored. Which means that after going further down than 2 nodes (4 nodes, 8 nodes)
# we would have to basically get the closest right to the closest left, and so on.
# First we would declare left_base and right_bases, the reason being our root, and it's two children don't really matter. We need to actually be caring about the symmetry
# after the root and it's children.
# If both the children don't exist, and it's just the root, then we would return True and if one of the children exists but the other doesn't, we'd return False as is
# because that wouldn't be symmetrical.
# After that, we just follow the skeleton of the same_tree.py, calling left_base.left on left_base and right_base.right as right_base further down. That would be the outer
# match since farthest left has to match farther right.
# The opposite would be true in inner_match case so we would call left_base's right and right_base's left.
# Finally we chain all them together just like the previous problem.