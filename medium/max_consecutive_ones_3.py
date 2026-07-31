class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left = right = 0
        window_dict = {0:0, 1:0}
        for right in range(len(nums)):
            window_dict[nums[right]] += 1
            one_values = window_dict[1]
            if right-left+1-one_values > k:
                window_dict[nums[left]] -= 1
                left += 1
        return right-left+1

# So we just need to find the longest array of 1s after flipping. We can simply use the technique we did in maximise_the_confusion_of_an_exam.py
# except we only need to check 1s, therefore we'll only take window_dict[1]. We'll subtract the ones from the length of the window and see if
# that's bigger than k.
# We do this because we need to find at most k zeros, therefore this helps us find the greatest window with only k occurrences of zero.