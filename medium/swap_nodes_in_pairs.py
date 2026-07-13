# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        length_current = head
        length = 0

        while length_current:
            length += 1
            length_current = length_current.next

        if length < 2:
            return head

        result = head.next
        prev_pair_tail = None
        switching_current = head

        for x in range(0, length // 2):
            first = switching_current
            second = switching_current.next
            next_pair_head = second.next

            second.next = first
            first.next = next_pair_head

            if prev_pair_tail:
                prev_pair_tail.next = second

            prev_pair_tail = first
            switching_current = next_pair_head

        return result

# The first thing we need to know is a swapping algorithm/codeblock. We learnt this in bubblesort that:
# temp = s[y+1], s[y+1] = s[y], s[y] = temp
# Therefore, we can apply the same in this problem for swapping.
# Firstly, we'll calculate the length of the linked list. This will help us find out how many swaps are needed.
# If the length of the list is 0 or 1, no swaps can be done so we'll just return head as is. Otherwise, we'll do the computation.
# We'll set result as head.next, this is what we'll eventually be returning.
# We'll set the prev_pair_tail as None and the switching_current = head, this is our pointer for the "pair" essentially.
# We'll declare first as switching_current and then the second node as switching_current.next.
# We'll store second.next in next_pair_head before switching it to first.
# Then we'll just do the "bubblesort-ish swap". second.next will point back to first, and first will now just point to the next_pair_head.
# However, we need to keep one thing in mind that, the heads of the next pairs can be changed. For example:
# in 1->2->3->4, once we swap 2->1->3->4, when we go onto swap 3->4 to 4->3, 1 would still be pointing at 3 and would not switch to 4.
# Therefore, we need a prev_pair_tail, which in this case is basically 1.
# If prev_pair_tail exists, then we'll set it to second, meaning 1->4.
# We'll just declare prev_pair_tail as first and then increment the switching_current to the next_pair_head to move onto the next pair.