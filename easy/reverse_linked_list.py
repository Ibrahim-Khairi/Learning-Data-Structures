# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        previous = None
        current = head

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous

# We simply need to change .next values to the previous.
# Firstly, we'll initialize two pointers - previous being the pointer that points to the previous node and current being the pointer that
# points to the current node.
# Secondly, we'll run a loop till we reach the end of the list, in other words, till current becomes null.
# First, we'll store the current.next into temp. That way, we can change current.next to previous without losing the element/node it was
# originally pointing at or linked with. Once we've changed current.next to the previous node, we can now say previous has become current,
# and we can increment current using current = temp (where we previously stored the original current.next).
# Now, since we have reached the end of the list, the previous is currently at the start of originally the LAST node. Therefore, previous is
# our new head and we can just return that.