# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        values_match = p.val == q.val
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        return values_match and left_same and right_same

# So we need to simply verify every single node's value with either of the trees.
# Firstly, if either roots don't exist at all, we would just return True because yes those are same trees even if they aren't really trees at all, lol.
# Secondly, if one of the roots exists but the other doesn't, that would automatically become different, so we return False as is.
# We would match the values by saying p.val == q.val and assign that to a boolean result as values_match, and we would be using this later in our return statement to chain
# the variables together.
# left_same would just be calling the recursion on the left nodes of both p and q. Same with right_same.
# At the end we would just chain them all together with left_same and right_same serving as our recursions and values_match being our actual "true" or "false" operative.