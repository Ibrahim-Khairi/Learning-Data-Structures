class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        zero_count = 0
        answer = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            answer = max(answer, right-left)

        return answer

# So this is a fairly simple problem that requires just checking the largest window size that contains at most one occurrence of 0, since we are
# only allowed to delete exactly one element.
# So, we declare a left pointer, a zero_count counter variable, and an answer variable to be returned.
# We loop the right pointer through the entire nums array, and check whether each element is 0. If it is, then we just increment the counter.
# We then keep a while loop to check that the zero_count should remain more than 1.
# As long as it's more than 1, we'll shrink the window from left, checking if the left pointer is at a 0. If it is, then we'll decrement the
# counter variable, and once we are out of the selection statement, we'll just advance left forwards. At the very end of the iteration, we'll
# just check the distance between right-left and compare it with our answer already. We'll then update the value of answer to take the bigger
# out of the two, so we get the longest subarray as our answer.