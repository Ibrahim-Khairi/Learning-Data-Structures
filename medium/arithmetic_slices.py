class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 3:
            return 0

        arithmetic_subarrays = 0
        difference_between_consecutives = 0

        for right in range(2, len(nums)):
            if right > 0 and nums[right] - nums[right-1] == nums[right-1] - nums[right-2]:
                difference_between_consecutives += 1
            else:
                difference_between_consecutives = 0
            arithmetic_subarrays += difference_between_consecutives

        return arithmetic_subarrays

# So we essentially just need to see whether 3 elements have the same difference or not. It's very similar to the
# number_of_smooth_descent_periods_of_a_stock.py, where we just have to get a streak of consecutive elements with the same difference.
# Firstly, we know that a subarray needs to consist of at least three elements - therefore, if nums if less than 3, we can just return
# 0. After that, we'll draw up an arithmetic_subarrays counter variable, and a difference_between_consecutives that would serve as
# a streak variable - originally set to 0. We'll then loop right from 2 to len(nums) since we need to check right with right-1 and
# right-1 with right-2. If right is obviously greater than 0, and the difference between nums[right] and nums[right-1] is the same
# as nums[right-1] and nums[right-2], then we'll just add to the streak.
# After that, we can just add the streak to the arithmetic_subarrays. 