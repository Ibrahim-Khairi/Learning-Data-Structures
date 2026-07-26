class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        distinct_elements = len(set(nums))

        left = 0
        substring_count = 0
        window_dict = {}
        for right in range(len(nums)):
            window_dict[nums[right]] = window_dict.get(nums[right], 0) + 1
            while len(window_dict) == distinct_elements:
                window_dict[nums[left]] -= 1
                if window_dict.get(nums[left]) == 0:
                    window_dict.pop(nums[left])
                left += 1
            substring_count += left

        return substring_count

# The first thing we need to do is find out the number of distinct elements in the subarray. This is what we'll be equating with our sliding
# window.
# We'll then declare a left pointer, substring_count counter variable, and a window_dict that tracks the elements and their frequencies in our
# sliding window.
# We'll then loop our right pointer through the entire array, adding to the frequency of nums[right] or declaring a new key for it, if it doesn't
# exist already.
# Then we'll draw a while loop that ensures that the len(window_dict) is equals to the distinct_elements variable that was the length of the set.
# This ensures that all distinct elements are existing in the window. While that condition remains true, we can keep removing from the left.
# If the key at the left happens to go all the way down to 0 as it's frequency due to decrementing, we'll just remove that key using .pop(), and
# increment the left pointer within that same loop.
# Once we are out of the inner while loop, at the very end of the iteration of the first loop, we can just increment substring_count with whatever
# our left variable is, using the same logic that we did in number_of_substrings_containing_all_three_characters.py.