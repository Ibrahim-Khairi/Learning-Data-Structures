# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        accessed = set()
        tail = head

        while tail:
            if tail not in accessed:
                accessed.add(tail)
                tail = tail.next
            else:
                break

        if tail:
            return True
        else:
            return False

# So we learned about a new type of data structure in python - set() which allows you to store things like a dictionary but instead of keeping
# the values paired with the keys, you just keep the keys. Dictionaries and Sets give fast "in" lookups, in comparison to an array that goes
# element by element making it slower.
# So instead of storing the tail.val in the set, we can just store the entire node itself and then if the cycle goes back to that node we
# can see whether it already exists in set. If it does, we can break out of the loop, and since tail would be a null element we can just
# return False.