class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        left = 0

        window_set = set()
        for right in range(len(nums)):
            if nums[right] in window_set:
                return True
            else:
                window_set.add(nums[right])

            if len(window_set) > k:
                window_set.remove(nums[left])
                left += 1

        return False

# We'll initialize a left pointer and a window_set.
# We'll iterate right from 0->len(nums) and each iteration we'll check if right is in window_set. If it happens to be in the window_set then
# it means that the indices are different and the values are same, so we can just return True as is.
# Otherwise, we'll add right to the window_set.
# If the window_set exceeds k, meaning if the window is more than the defined size, then we'll shrink it from the left, and remove left from the
# window_set, and increment the left pointer.
# If, after all the iterations are done, we still haven't found a duplicate and no True has been returned, we can just return False.