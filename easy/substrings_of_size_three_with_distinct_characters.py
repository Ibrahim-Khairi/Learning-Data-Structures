class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        left = 0
        right = 3

        good_strings = 0

        if len(set(s[left:right])) == 3:
            good_strings += 1

        for right in range(3, len(s)):
            left += 1
            if len(set(s[left:right+1])) == 3:
                good_strings += 1

        return good_strings

# This is a fixed-window problem.
# The problem states that the window should always be size 3. Therefore, we can do the initial check from 0->3 and see whether a set has distinct
# characters. If the length of the set is 3, that means it has 3 distinct characters, otherwise it would be 2 or 1.
# We can keep a good_strings counter that we can increment each time our set is length 3.
# We'll do the same check from 3->len(s).