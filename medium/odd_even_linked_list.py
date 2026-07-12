# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current = head
        even_array = []
        odd_array = []

        pointer = 0
        while current:
            pointer += 1
            if pointer % 2 == 0:
                even_array.append(current)
            elif pointer % 2 == 1:
                odd_array.append(current)
            current = current.next

        new_list = ListNode()
        new_current = new_list

        for x in range(0, len(odd_array)):
            new_current.next = odd_array[x]
            new_current = new_current.next
        for x in range(0, len(even_array)):
            new_current.next = even_array[x]
            new_current = new_current.next
        new_current.next = None

        return new_list.next

# Basically, we just need to put all odd nodes on one side, and all even nodes on one side.
# Every 1st, 3rd, 5th, 7th node... will be an odd.
# Every 2nd, 4th, 6th, 8th node... will be an even.
# Therefore, we can just declare a pointer to keep track of which type of node we are add and accordingly append it into an array
# designated for odd nodes/even nodes. We can do this for the entirety of the list.
# Then we can just declare a new linked list, and we can then append the odd nodes first from the odd_array, and then the even nodes later
# from the even_array.