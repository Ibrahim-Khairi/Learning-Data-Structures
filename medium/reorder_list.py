# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        # Count length
        length = 0
        counter = head
        while counter:
            length += 1
            counter = counter.next

        if length > 1:
            # Duplicate the original list
            duplicating_current = head
            duplicate_list = ListNode()
            new_current = duplicate_list

            while duplicating_current:
                new_current.next = ListNode(duplicating_current.val)
                new_current = new_current.next
                duplicating_current = duplicating_current.next

            # Reverse the duplicated list
            reversing_duplicate_current = duplicate_list.next
            reversing_duplicate_previous = None

            while reversing_duplicate_current:
                temp = reversing_duplicate_current.next
                reversing_duplicate_current.next = reversing_duplicate_previous
                reversing_duplicate_previous = reversing_duplicate_current
                reversing_duplicate_current = temp

            # Now we can compute using the two pointers
            reading_current = head
            last_node = None

            for x in range(0, length//2):
                temp1 = reading_current.next
                temp2 = reversing_duplicate_previous.next

                reading_current.next = reversing_duplicate_previous
                reversing_duplicate_previous.next = temp1

                last_node = reversing_duplicate_previous

                reading_current = temp1
                reversing_duplicate_previous = temp2

            if length % 2 == 1:
                last_node.next = reading_current
                last_node = reading_current

            last_node.next = None

        return head

# The first thing that we need to do is figure out the length of the list.
# The next thing we need to is duplicate the list. We can do this by declaring duplicate_list as ListNode() and then instead of making the
# head of that duplicate_list our original's list head, we'll make it a ListNode using the original's list head's VALUE. This is very
# important as it makes sure that we are not altering the original list itself, and are actually just declaring a duplicate list with
# the values of the nodes in our original list.
# Once we are done duplicating the list, we can reverse it.
# After we are done with reversing, we'll declare a new variable this time at the head of our original list. This will be the pointer that
# iterates through our original list, whereas reversing_duplicate_previous is the pointer that ends up as the head of our reversed duplicate
# list. We'll also declare a last_node as None, this is going to be crucial to close the linked_list off and to connect the middle node in
# cases where the length is odd-digited, i.e. 5,7,etc.
# We'll store their .nexts in temp variables, and we'll link reading_current's next to reading_duplicate_previous. Next, we can link
# reading_duplicate_previous's next to the temp1 that we stored.
# So let's consider the example 1->2->3->4->5, which reversed would be 5->4->3->2->1.
# Initially, out reading_current is 1, and our reversing_duplicate_current is 5.
# We'll store the links between 1->2 and 5->4 in temp1 and temp2, respectively.
# Then we'll link reading_current to reversing_duplicate_current, so 1->5->....
# After that, we can just link reversing_duplicate_current back to temp1 (->2...).
# So it would become something like 1->5->2->....
# Our last_node becomes the reversing_duplicate_current, which is 5 in this case.
# Then, we just increment the pointers. This can be done using the temp variables that we stored the links ahead at the start. So,
# reading_current becomes 2 and reversing_duplicate_current becomes 4.
# Then this iteration happens for one more time, since our for loop runs for 0->len//2 (2) so 0,1.
# Afterwards, we are only left with 3 that the reading_current sits at after we increment the pointers. Now, we can link the last_node to
# that. So the last_node was 4, and now it becomes 4->3, making the list 1->5->2->4->3. And then we can just make 3 our last_node, after
# which we can just close the list off. So it becomes 1->5->2->4->3->None.
# Now we can just return our head as is. If the input list happens to be only one integer, then we can just return it as it is, because
# nothing needs to be ordered.