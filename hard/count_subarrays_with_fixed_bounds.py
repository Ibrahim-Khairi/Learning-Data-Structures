class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """

        subarray_count = 0
        last_min_index = last_max_index = last_bad_index = -1

        for right in range(len(nums)):
            if nums[right] == minK:
                last_min_index = right
            if nums[right] == maxK:
                last_max_index = right
            if nums[right] > maxK or nums[right] < minK:
                last_bad_index = right
            subarray_count += max(min(last_min_index, last_max_index) - last_bad_index, 0)

        return subarray_count

# So we'll initialize a subarray_count counter variable to be returned, and we'll initialize all the indexes as -1 which is not a valid array
# index (0->len(nums)-1), therefore, that suits us.
# The three indexes -> last_min_index shows the most recent index value equal to minK. last_max_index shows the most recent index value equal to
# maxK. finally, last_bad_index shows the most recent index value where we come across a value outside the [minK,maxK] range entirely. For example,
# if we are given a nums array [1,5,6,10] with minK as 5 and maxK as 6, then our "bad values" are 1 and 10.
# We then iterate through the nums array, slotting every element into it's particular index. If it matches minK, it enters the last_min_index slot,
# if it matches maxK, it enters the last_max_index slot, and if it's smaller than minK or greater than maxK, then it's out of our fixed bounds so,
# we put right as our last_bad_index.
# Now we know last_bad_index is not going to be part of our valid subarrays, in whatever way. Also, if it breaks a contiguous part where the other
# elements are still within the minK to maxK range, then everything would still be invalid.
# So, we can not have a subarray that starts at or before the last_bad_index, otherwise the last_bad_index would be a part of the subarray.
# Consider an array [2,3,5,8,9], minK = 5, maxK = 9. Our first last_bad_index would be 0 (2), because we can not have a valid subarray with 2 in it
# since it's outside the 5->9 range. Then our second last_bad_index would be 1 (3), again because we can not have a valid subarray with 3 in it.
# Given that, it is obvious that 2 will also, therefore, not be part of the array on the same iteration.
# So, since we know anything before or at last_bad_index is invalid, we can keep that as a subtractive term. Now, we know the window needs to
# have minK and maxK in it. Any subarray will not start before last_min_index or before last_max_index, otherwise we would leave the minK or maxK
# element behind us and not include that in the subarray.
# Therefore, we need to find which one is smaller, the last_min_index or the last_max_index. The reason we can't just pick a last_max_index is
# because, the array is not sorted, therefore, maxK can appear before minK. Like in this array -> [6,5,2,1,4] minK = 1 and maxK = 5.
# Once we've found out which one is smaller through min(last_min_index, last_max_index), we can subtract last_bad_index from it, since our subarray
# would start after last_bad_index and at or before last_min_index or last_max_index, given whichever one is earlier.
# Hence, we'll just add that into subarray_count. If the last_bad_index is AFTER the last_min_index/last_max_index, the computed result would be
# in negative, therefore adding that to subarray_count, would reduce it, instead. Therefore, we'll ensure that
# min(last_min_index, last_max_index)-last_bad_index is NOT less than 0 before adding it into subarray_count. We just do that simply with max().