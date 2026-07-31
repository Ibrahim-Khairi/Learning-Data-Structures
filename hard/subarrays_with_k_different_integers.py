class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k == 0:
            return 0

        left = 0
        window_dict = {}
        first_total = 0

        for right in range(len(nums)):
            window_dict[nums[right]] = window_dict.get(nums[right], 0) + 1
            while len(window_dict) > k:
                window_dict[nums[left]] -= 1
                if window_dict[nums[left]] == 0:
                    window_dict.pop(nums[left])
                left += 1
            first_total += right - left + 1

        left = 0
        window_dict = {}
        second_total = 0

        for right in range(len(nums)):
            window_dict[nums[right]] = window_dict.get(nums[right], 0) + 1
            while len(window_dict) > k-1:
                window_dict[nums[left]] -= 1
                if window_dict[nums[left]] == 0:
                    window_dict.pop(nums[left])
                left += 1
            second_total += right - left + 1

        return first_total - second_total

# Okay so if there are 0 different integers in an array, then we can just return 0 since there wouldn't be a good subarray anyway.
# Now, this sort of requires you to sort of change both pointers.
# Consider [1,2,1,2,3] with k=2.
# [1,2] in [1,2,1,2,3] -> the first 1,2
# [1,2,1] in [1,2,1,2,3] -> the first 1,2,1
# [1,2,1,2] in [1,2,1,2,3] -> the first 1,2,1
# [2,1] in [1,2,1,2,3] -> the first 1 goes away. the last 2 goes away. 2,1
# [2,1,2] in [1,2,1,2,3] -> we add the 2 back. 2,1,2
# [1,2] in [1,2,1,2,3] -> we remove the first 2 and keep the added back 2. 1,2
# [2,3] in [1,2,1,2,3] -> we remove the 1, keep the added 2 back 2, and just add in 3. 2,3
# Therefore, it's not a linear growth for right.
# So, now imagine if you end at right = 3 and just keep incrementing left. How many distinct elements would you end up with?
# [1,2,1,3] -> 3 distinct -> 3 <= k. (1)
# [2,1,3] -> 3 distinct -> 3 <= k. (2)
# [1,3] -> 2 distinct -> 2 <= k. (3)
# This means, at right = 3, we'll have at most 3 distinct elements. No more, only either at exactly 3 or less than 3.
# Now imagine, if we wanted at most 2 distinct elements. So let's make k = 2.
# # [1,2,1,3] -> 3 distinct -> 3 > k. (No)
# # [2,1,3] -> 3 distinct -> 3 > k. (No)
# # [1,3] -> 2 distinct -> 2 <= k. (1)
# This implies that between at most 3 and at most 2, the first two iterations of [1,2,1,3] and [2,1,3] are the ones that are valid with 3 distinct
# elements. Therefore, to get the substrings that are valid with k distinct elements, we need at most(k) - at most(k-1).
# So now, we just need to compute two at most loops. Which we can do with 2 sliding window templates.
# One would be checking the length of the window against k (len_window > k), and the other would be checking the length of the window against k-1
# (len(window_dict) > k-1). len(window_dict) just gives you back the number of keys you have in the window_dict which would mean the amount of
# distinct elements we are talking about. If the amount of distinct elements exceeds k, that would violate the at most k policy so we can just
# start shrinking from the left.
# We'll compute the two totals at the end and then just subtract the totals to get at most(k) - at most(k-1) that we talked about previously.