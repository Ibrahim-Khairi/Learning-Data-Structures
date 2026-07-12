# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        result = ListNode()
        head = result

        carry = 0
        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            sum = digit1 + digit2 + carry
            carry = sum // 10
            sum = sum % 10

            head.next = ListNode(sum)

            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next

# So it kind of works exactly like how normal addition works. We just need to worry about carry.
# Let's consider 8+4 = 12. In this case, we write down 1 and 2 becomes what we carry over. So basically, we need to find a way to separate
# the 1 and 2. We can do that with // and %. If we do 12 // 10, we get 1.2, which eventually becomes 1 because of floor division. To get
# the 2, we can just use modulus and do 12 % 10, which gives 2.
# Now we'll initialise an empty linked list which we'll use to append these calculated digits in.
# Then we initially declare carry as 0. Now we essentially have 3 numbers/digits to worry about. The first linked list digit, the second
# linked list digit, and the carry. If either of these 3 digits exist, we need to do a computation. Therefore, that'll become our loop
# condition. Now we'll just declare our digit1 and digit2 if the node exists in either linked list or not. Then we'll do the summation
# and figure out the carry using the analogy we talked about before. Afterwards, we can just make a new node and shift onto that, and
# update the linked list pointers forward to move on to the next digits.