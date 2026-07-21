class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        left = 0
        right = k
        window_state = sum(nums[left:right])
        max_avg = window_state/float(k)

        for right in range(k, len(nums)):
            window_state -= nums[left]
            window_state += nums[right]
            if window_state/float(k) > max_avg:
                max_avg = window_state/float(k)
            left += 1

        return max_avg

# So this is a fixed-window sliding window problem. I had to learn the entire concept for this, because it's entirely new to me.
# We've to basically maintain a window of size k and sum all elements within it, to then divide it by k to derive the average. We'll maintain
# a max_avg variable to see whether the current average is greater than max_avg.
# We'll initially declare left and right, and the initial window_state and max_avg.
# Then we'll loop right from k->len(nums), putting each right in window_state (which is basically the sum of the elements within the window),
# and taking left out of it.
# Every iteration, we'll increase left and do the check talked about previously. At the end of the loop, we'll have checked all possible windows.