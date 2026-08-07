class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        window_dict = {}
        window_sum = max_sum = left = 0
        for right in range(len(nums)):
            window_dict[nums[right]] = window_dict.get(nums[right], 0) + 1
            while window_dict[nums[right]] > 1:
                window_sum -= nums[left]
                window_dict[nums[left]] -= 1
                if window_dict[nums[left]] == 0:
                    window_dict.pop(nums[left])
                left += 1
            window_sum += nums[right]
            max_sum = max(max_sum, window_sum)

        return max_sum

# In simpler terms, we just need the sliding window with no repeated elements and the biggest sum of all the elements within it.
# Therefore, we'll declare a window_dict to check the frequency of the elements, a window_sum to keep track of the sum of the elements
# within the window, and a max_sum variable to be returned.
# We iterate through each element, appending it into the dictionary. Then we check if the frequency/value of that element is greater
# than 1, since only unique elements are allowed. While it's greater than 1, we can keep shrinking from the left. At every shrink,
# we'll decrement the window_sum by the element on the left, and reduce the value of the window_dict[nums[left]] and pop it, if it
# becomes zero, and increment the left pointer.
# Once we are done with these computations, we can just add nums[right] to the window_sum and check whether that current window_sum
# is bigger than the previously max_sum.