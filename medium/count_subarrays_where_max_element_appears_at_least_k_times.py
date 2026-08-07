class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        max_number = -float('inf')
        for x in nums:
            max_number = max(x, max_number)

        left = subarray_count = max_number_count = 0
        for right in range(len(nums)):
            if nums[right] == max_number:
                max_number_count += 1
            while max_number_count == k:
                if nums[left] == max_number:
                    max_number_count -= 1
                left += 1
            subarray_count += left

        return subarray_count

# We first need to get the maximum element of nums to check whether it appears at least k times in a subarray. To do that, we'll just
# run a basic for loop and get the biggest element of nums.
# Afterwards, we'll run a sliding window with 2 variables initialized (apart from the left pointer). The first will be the
# subarray_count to be returned, and the second one is the max_number_count. At each iteration of right, we'll check whether the current
# element is the max_number and accordingly increment max_number_count. We'll then check if the max_number_count is equals to k. Since
# that satisfies the at least k condition, we can now start shrinking from the left. At the end of the iteration, we can just add
# left to the subarray_count because the loop would terminate exactly where the condition of at least k fails. Therefore, everything
# element before that is a valid subarray, and we can just add left to the subarray_count.