# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        length_current = head
        length = 0

        while length_current:
            length += 1
            length_current = length_current.next

        node_to_remove = length - n + 1

        if node_to_remove != 1:
            reading_current = head
            previous = None
            pointer = 1

            while reading_current and pointer < node_to_remove:
                previous = reading_current
                reading_current = reading_current.next
                pointer += 1

            previous.next = reading_current.next

            return head
        else:
            head = head.next

            return head

# So the first thing we do, is figure out the length of the list.
# After that we derive a formula to figure out which node to remove => length - n + 1
# Then we can just initialise a counter variable (pointer) and keep iterating till we reach the desired node.
# Our reading_current resides on the node to be removed. So we can just set previous.next to reading_current.next, de-linking that node
# permanently.
# If the node to be removed is basically the first node, then we can just like move the head forwards as it is. That'll advance the entire
# list forward.