class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        number_of_ones = 0
        for x in nums:
            if x == 1:
                number_of_ones += 1

        left = 0
        number_of_ones_in_window = max_number_of_ones_in_window = 0
        for right in range(2*len(nums)):
            if nums[right % len(nums)] == 1:
                number_of_ones_in_window += 1
            if right-left+1 > number_of_ones:
                if nums[left % len(nums)] == 1:
                    number_of_ones_in_window -= 1
                left += 1
            max_number_of_ones_in_window = max(number_of_ones_in_window, max_number_of_ones_in_window)

        return number_of_ones - max_number_of_ones_in_window

# In order to group all the 1s together, we can essentially do something which involves finding the total number of ones in the list
# and then running a window of that size across the list. We then need to find which window has the most 1s.
# In order to that with a circular array, we need have two options: either we can extend the nums array by doubling the array,
# like we did in alternating_groups_1.py. However, that takes more space. Another way we can do that is if we get right % len(nums).
# That way, we can maintain right within the index bounds while still iterating across the array circularly.
# So, we run a sliding window as per normal, doubling the len(nums) to circulate the array in the for loop.
# We can then just check as per normally nums[right] == 1: and add it to number_of_ones_in_window. If the length of the window gets
# bigger than the total number_of_ones that we found initially, we can just shrink from the left.
# At the very end of the iteration, we can just check whether the current window has more windows than our previous max.
# In order to account for the circular array, we can mod both the pointers (right and left) with len(nums) in both places, where we
# are incrementing the number_of_ones_in_window, and where we are decrementing it from the left.
# We can then just return the subtraction of total ones with the window with most 1s in it.