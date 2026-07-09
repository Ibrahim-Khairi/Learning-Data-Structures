# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        head = ListNode()
        current = head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return head.next

# Initially, I was trying to go for merge it into list1 approach. So the solution was kind of looking like what's down below. However
# there was an issue since we were never linking the previous node to the new node after a comparison. So like if list1[5] and list2[1,2,4],
# we were doing 1->5 and then 2->5, but we were never linking 1->2 which would then sort of make it 1->2->5 before working out the rest of
# the remaining nodes.
# current1 = None
# current2 = None
# head = None
#
# if list1 and list2:
#     current1 = list1
#     current2 = list2
#     if list1.val > list2.val:
#         head = list2
#     else:
#         head = list1
# elif list1 and not list2:
#     current1 = list1
#     head = list1
# elif list2 and not list1:
#     current2 = list2
#     head = list2
#
# while current1 or current2:
#     if current1 and current2:
#         if current1.val < current2.val:
#             temp = current1.next
#             current1.next = current2
#             current1 = temp
#         elif current1.val > current2.val:
#             temp = current2.next
#             current2.next = current1
#             current2 = temp
#         elif current1.val == current2.val:
#             temp = current1.next
#             current1.next = current2
#             current1 = temp
#     elif current1:
#         current1 = current1.next
#     elif current2:
#         current2 = current2.next
#
# if head:
#     return head
# else:
#     return None
# The current approach basically involves making a new list entirely which is not explicitly stated by the question as prohibited.
# So we declare our head as the new list, and then declare our current pointer as that head.
# Then while there are still elements remaining in both the lists, we check conditions. If list1 node's value is smaller than list2
# node's value, then we can connect our current pointer to that node, and we can move the list1 onto the next node so that it completely
# unlinks with this node that we have already linked with the current.
# We do the vice versa if list1.val >= list2.val so we can just use an else statement.
# Once the comparisons are done, we can just increment the current to now start putting nodes at the next spot upon the next iteration.
# After coming out of the loop, we need to deal with 2 cases. If one list is empty, but the other one still has nodes left, then we can
# just link our current.next to that entire list.
# So imagine list1 [1,2,4] and list2 as [3,5,6,7,8]
# Our list1 has 3 nodes only so after 4 iterations we'll be looking at head [1,2,3,4] but list2 still has [5,6,7,8] remaining. Therefore,
# we can then just append that list2 entirely with our current.next.