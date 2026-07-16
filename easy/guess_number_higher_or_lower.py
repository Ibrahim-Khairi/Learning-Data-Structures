# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        upperbound = n
        lowerbound = 1
        mid = 0

        while lowerbound <= upperbound:
            mid = (lowerbound + upperbound) // 2

            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                upperbound = mid - 1
            elif guess(mid) == 1:
                lowerbound = mid + 1

        return mid

# Very similar to first_bad_version.py.
# Simple binary search dependent on the return value that the guess API gives us.