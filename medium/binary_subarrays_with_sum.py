class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        left = 0
        window_sum = 0
        first_substring_count = 0

        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum > goal:
                window_sum -= nums[left]
                left += 1
            first_substring_count += right-left+1

        left = 0
        window_sum = 0
        second_substring_count = 0

        if goal-1 < 0:
            second_substring_count = 0
        else:
            for right in range(len(nums)):
                window_sum += nums[right]
                while window_sum > goal-1:
                    window_sum -= nums[left]
                    left += 1
                second_substring_count += right-left+1

        return first_substring_count - second_substring_count

# So we just need subarrays with the sum of their elements being exactly the same as goal.
# In order to achieve that, we can just run the at most simulation that we did in the hard problem before,
# hard/subarrays_with_k_different_integers.py
# In this, all we really need is a window_sum sum variable that we can keep incrementing with right, and then while it exceeds goal, we'll keep
# shrinking it from the left. At the end, we'll just store the window_length in a substring_count variable.
# Then, we run it back and do it all over again, only this time it's goal-1. This is because we need to account for the exceeds that got added
# into right-left+1. Again, the same logic as before, really.
# And then at the end, we just subtract the two substring counts.