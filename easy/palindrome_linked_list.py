# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        length_current = head
        length = 0
        while length_current:
            length_current = length_current.next
            length += 1

        reading_current = head
        pointer = 0
        array = []

        middle = length // 2
        if length % 2 == 0:
            while reading_current and pointer < middle:
                array.append(reading_current.val)
                reading_current = reading_current.next
                pointer += 1

            while reading_current:
                if array:
                    if reading_current.val == array[-1]:
                        reading_current = reading_current.next
                        array.pop()
                    else:
                        return False
                else:
                    return True
        else:
            while reading_current and pointer < middle:
                array.append(reading_current.val)
                reading_current = reading_current.next
                pointer += 1
            array.append(reading_current.val)

            while reading_current:
                if array:
                    if reading_current.val == array[-1]:
                        reading_current = reading_current.next
                        array.pop()
                    else:
                        return False
                else:
                    return True

        return True

# We basically do almost about everything just as we did in middle_of_the_linked_list.py to find out the middle and iterate until it.
# Every iteration we'll append the value into an array.
# Once we are done with that, we'll iterate through the other half of the list, comparing it with every single element at the top of the
# array. If they are similar, we'll increment the pointer and pop out the corresponding element from the array.
# The second we find any discrepancies, we can just terminate everything and return False.