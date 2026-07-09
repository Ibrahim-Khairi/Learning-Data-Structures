# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next

# This has to be the easiest medium problem I've ever seen bro.
# We've been given the node, and we need to figure out how to link the previous node to node.next.
# However, since we don't have any way of getting the previous, we need another way.
# What we can do is, we can copy the value of the node next to node into node.
# And then literally just point node.next to the next node of node.next, which is node.next.next.