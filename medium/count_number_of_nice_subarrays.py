class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left = 0
        odd_count = 0
        first_subarray_count = 0

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1
            while odd_count > k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1
            first_subarray_count += right-left+1

        left = 0
        odd_count = 0
        second_subarray_count = 0

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1
            while odd_count > k-1:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1
            second_subarray_count += right-left+1

        return first_subarray_count - second_subarray_count

# Since we need to find exactly k odd numbers in a subarray, we are aiming for the at most(k) - at most(k-1) approach that we talked about
# previously in subarrays_with_k_different_integers. We simply need odd_count to be our window state, which is the sum of the odd numbers that we
# have, and we'll be checking this against k or k-1. In the case it's big, we'll shrink the window from the left and decrement odd_count
# accordingly.
# At the very end, we'll return the subtraction of the first_subarray_count, calculated with k, and the second_subarray_count, calculated with k-1.
