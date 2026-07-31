class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left = 0
        window_dict = {}
        good_subarrays = 0
        pairs_count = 0

        for right in range(len(nums)):
            pairs_count += window_dict.get(nums[right], 0)
            window_dict[nums[right]] = window_dict.get(nums[right], 0) + 1
            while pairs_count >= k:
                window_dict[nums[left]] -= 1
                pairs_count -= window_dict[nums[left]]
                if window_dict[nums[left]] == 0:
                    window_dict.pop(nums[left])
                left += 1
            good_subarrays += left

        return good_subarrays

# This is honestly a bit tricky. The problem is, elements can overlap. So if 0,1 indices make a pair, then 1,2 can also make a pair.
# Therefore, what we do is, we initialize a variable pairs_count counter, that we increment by each key's values. If the key doesn't exist, then
# it just gets added a 0 to it, since that isn't a pair. Then we just simply add nums[right] to our dictionary.
# We then check whether the pairs_count is greater than or equals to k, since it says a subarray is good if there are AT LEAST k pairs of indices.
# While it's greater than or equals to k, we'll be shrinking from the left and also decrementing nums[left] from the pairs_count. We can then just
# add left itself to good_subarrays, since everything before the window is actually good.