# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        length_current = head
        length = 0
        while length_current:
            length_current = length_current.next
            length += 1

        reading_current = head
        middle = length // 2
        pointer = 0

        while reading_current and pointer < middle:
            reading_current = reading_current.next
            pointer += 1
        return reading_current

# The first thing we do is calculate the length of the linked list by going through it and incrementing a counter variable (length).
# Then, we declare another current this time at head again, and this will be the node we return.
# Afterwards, we calculate the middle, and this is what we are going to use to compare with the new counter variable we declare (pointer).
# While pointer remains less than middle, we'll keep incrementing it.
# Once the loop ends, we have reached the middle of the list, therefore, we can simply return it.
# At first, however, I tried checking whether length is even or not using modulus (length % 2 == 0) but it wasn't necessary apparently.