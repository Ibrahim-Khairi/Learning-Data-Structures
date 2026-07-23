class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """

        nums = str(num)

        divisor_substrings = 0

        left = 0
        for right in range(k-1, len(nums)):
            if (right-left+1) <= k:
                substring = nums[left:right+1]
                if int(substring) != 0 and num % int(substring) == 0:
                    divisor_substrings += 1
            left += 1

        return divisor_substrings

# The first thing we need to do is convert num into string, so that we can iterate through each digit of it.
# Since this is a fixed-window problem, we can start iterating right from k-1 to len(nums) and the second the window size exceeds k, we can just
# shrink from the left.
# If the window size is within k, then we can take the entire window as the substring, so left->right+1.
# Afterwards, we can ensure that the substring doesn't equate to 0 to avoid zero division. If it's not 0, then we can just divide the num by
# the substring, and if the division leaves no remainder, that means it is a valid divisor, and we can add to the divisor_substrings count.