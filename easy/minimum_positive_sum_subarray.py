class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """

        min_sum = float('inf')
        for size in range(l, r+1):
            for right in range(size-1, len(nums)):
                left = right-size+1
                window_sum = sum(nums[left:right+1])
                if window_sum > 0:
                    min_sum = min(min_sum, window_sum)

        return -1 if min_sum == float('inf') else min_sum

# We initialize the min_sum as float('inf') which is basically an integer so large, that anything in reality would obviously be lesser than that.
# Then, we need a for loop for the size between l and r. Since r is inclusive, we do r+1.
# Then, we declare another for loop for the right pointer for the sliding window that we need. We'll start it from the size-1 and take it all the
# way upto the length of the nums array.
# We then calculate left which is obviously the size of the window (right-left+1). size is basically acting like the left pointer of our window.
# We can then just derive the window_sum and check if it's positive. If it's positive, then we'll just take the minimum of our current min_sum
# or the newly derived window_sum.
# At the end, if min_sum has not been updated, we'll just return -1, otherwise we'll return our finalized min_sum.