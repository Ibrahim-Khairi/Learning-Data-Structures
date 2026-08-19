# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def traverse(result, node):
            if node is None:
                return
            traverse(result, node.left)
            result.append(node.val)
            traverse(result, node.right)

        traverse(result, root)

        return result

# Binary trees are recursive in nature, so I had to kind of get more familiar with recursion.
# Inorder Traversal is just Left -> Root -> Right. So we need to do the recursion accordingly.
# Initialize the array to be returned. Check if node is None, that would be our base case to stop the recursion. The general cases would be spanning out and traversing left
# and right. Therefore, we'll make an inner function that actually calls itself, since the outer function actually has to return the array, or at least that's what I thought
# would be simpler.
# Then we just traverse and append in the right order. Finally, we'll call traverse on the root to actually start the recursion.