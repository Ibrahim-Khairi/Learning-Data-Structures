# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        lowerbound = 0
        upperbound = n
        mid = 0

        while lowerbound <= upperbound:
            mid = (lowerbound + upperbound) // 2

            if isBadVersion(mid) == True:
                upperbound = mid - 1
            else:
                lowerbound = mid + 1

        if lowerbound > upperbound:
            return lowerbound

        return mid

# This took me unusually long, because at first I was running a for loop to check every single element, without reading the fact you're
# supposed to minimize the API calls.
# So you implement a basic binary search, if mid turns out to be True that could mean two things:
# 1) It's the first bad version
# 2) It's one of the later bad versions AFTER the first one, because all versions after the first bad version will automatically be bad.
# Therefore, we can just declare mid-1 our upperbound.
# However, if mid turns out to be False, that means our first bad exists in the second half of the array.
# If lowerbound has crossed upperbound, then we can just return lowerbound. 