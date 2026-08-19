# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        result = []

        def traverse(result, node):
            if node is None:
                return
            traverse(result, node.left)
            traverse(result, node.right)
            result.append(node.val)

        traverse(result, root)

        return result

# Exact same thing as inorder, except the traversing order changes to Left -> Right -> Root.