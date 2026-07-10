# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current = head
        previous = None
        accessed = set()

        while current:
            if current.val not in accessed:
                accessed.add(current.val)
                previous = current
                current = current.next
            else:
                current = current.next
                previous.next = current

        return head

# So we'll declare two pointers and a set.
# The previous pointer's next will help us just completely skip a node.
# We can use the set to see if we've already added the value to the set or not.
# These linked list problems are slowly becoming easier bro, thank God.