# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        # 1) Calculate length of list
        # 2) Compute k after modding with length
        # 3) Reverse whole list
        # 4) Split at k
        # 5) Reverse each half again
        # 6) Connect the second half with the first half

        # Step 1
        current = head
        length = 0
        while current:
            length += 1
            current = current.next

        # Step 2
        temp2 = None
        if length != 0:
            k = k % length
            if k != 0:
                # Step 3
                previous = None
                current = head
                while current:
                    temp = current.next
                    current.next = previous
                    previous = current
                    current = temp

                # Step 4
                current = previous
                y = 0
                while current and y < k - 1:
                    current = current.next
                    y += 1
                temp2 = current.next
                current.next = None

                # Step 5
                first_previous = None
                first_current = previous
                while first_current:
                    temp = first_current.next
                    first_current.next = first_previous
                    first_previous = first_current
                    first_current = temp

                second_previous = None
                second_current = temp2
                while second_current:
                    temp = second_current.next
                    second_current.next = second_previous
                    second_previous = second_current
                    second_current = temp

                # Step 6
                current = first_previous
                while current.next:
                    current = current.next

                current.next = second_previous

                return first_previous
            else:
                return head
        else:
            return head

# This is where we incorporate all our previous knowledge. How two pointers work, how to reverse a string, how to rotate an array, how to
# loop through a list, how to reverse a list, literally everything.
# Firstly, we need to do calculate the length of the list. We can simply do that by declaring a count variable and
# incrementing it upon each iteration of current. Once the nodes are all done in the list, we'll derive the length of the list.
# Secondly, we need to compute k. For that we'll ensure we don't do zero division, so we'll validate length, and then we'll compute k. If k
# happens to be 0 after computing, then we can just simply return the list as is since there's no need for rotations.
# Thirdly, once we are done with computing k, we can reverse the entire list just like we did with an array. To do that we will use what we
# learned in reverse_linked_list.py. Simply keep changing the current.next to the previous. That way when we are done, previous will be our
# new head. This is important to remember. previous is our ENTIRE LIST'S head.
# Fourthly, we need to split the list at k. For that, we'll loop till k, then we will store the .next pointer in a variable and make that
# .next to None. To loop till k, we just need to declare a current, AT PREVIOUS WHICH IS OUR HEAD, and then we can keep going till k. For
# that, we need a counter variable to keep the iteration count in check. Once we have reached the desire module, we'll do exactly as planned.
# Store the .next, and point the .next to None.
# So now if a head originally was 1,2,3,4,5 with k=2, it becomes 5,4 -> None (List 1)    3, 2, 1 -> None (List 2). We have stored 4's next to
# 3 in temp2.
# Fifthly, we will now reverse both the lists again. The first list's head can be previous as is (so we use that for first_current) and the
# second's list head can be temp2 (so we use that for second_current).
# Finally, once we are done reversing both of them, we just need to join them.
# 4, 5 -> None and 1, 2, 3, -> None. first_previous is 4, and we need to link that to second_previous which is 1.
# Therefore, we can't just simply do first_previous.next = second_previous.
# So now, we need to do one final loop through the entire first list to reach the second last node. This is to ensure current.next is still
# not null. If we reach the last node, current.next will become invalid. Therefore, we won't be able to do another current.next.
# So, at the second last node, when we do current.next, we get the last node outside the loop. We can now simply do current.next and point
# that towards 1, which was second_previous. Therefore, current.next = second_previous.
# Now, we can return the entire list that's been connected again, which is first_previous (first_previous became our entire head starting at 4).
# This is the most tedious and longest dsa problem I think I have solved till yet. Funnily enough, I was actually able to do it. Hehe.