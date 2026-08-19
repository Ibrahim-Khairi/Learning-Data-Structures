# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def traverse(result, node):
            if node is None:
                return
            result.append(node.val)
            traverse(result, node.left)
            traverse(result, node.right)

        traverse(result, root)

        return result

# Exact same thing as inorder and postorder, except the traversing order changes to Root -> Left -> Right.