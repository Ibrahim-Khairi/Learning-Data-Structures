class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums = sorted(nums)

        min_difference = nums[k-1]-nums[0]

        for right in range(k, len(nums)):
            left = right-k+1
            min_difference = min(min_difference, nums[right]-nums[left])

        return min_difference

# So, the first thing we need to do is sort the problems. Then we initialize min_difference as the difference between the element k-1 and 0.
# Afterwards, we loop right from k->len(nums). We don't declare left beforehand, instead we just calculate it within the loop itself.
# the window size (k) is always k = right-left+1 (1 includes left). Therefore, if we re-arrange the formula to calculate left, we get
# left = right-k+1. The reason we do that is because we know, at any given time of our sliding window, the left pointer would be the smallest,
# and the right pointer would be the largest number. Therefore, we can do this for all sliding windows, taking the minimum of either the existing
# min_difference or by calculating the difference between the numbers that both of our pointers point to.