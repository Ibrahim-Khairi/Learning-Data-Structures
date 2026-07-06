class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        upperbound = x
        lowerbound = 0
        result = 0

        while lowerbound <= upperbound:
            mid = (lowerbound + upperbound) // 2
            if mid ** 2 > x:
                upperbound = mid - 1
            elif mid ** 2 < x:
                lowerbound = mid + 1
                result = mid
            else:
                return mid

        return result

# Firstly, we'll declare our upperbound as the number itself, and the lowerbound as 0.
# We'll declare a result variable as 0 too.
# We'll run a basic binary search trying to figure out if the square of mid is more than the number in question or lesser.
# In either cases we deal with the bounds accordingly. If it's lesser than the number then we'll also set result to be our mid. This is for
# non-exact square-roots.
# If our mid happens to be an exact square of the number then we can just return mid. Otherwise, if the loop ends we just return the result
# that was the last set mid before the loop ended and the bounds crossed each other.