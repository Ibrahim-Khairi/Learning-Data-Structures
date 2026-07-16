class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lowerbound = 0
        upperbound = len(nums)
        while lowerbound < upperbound:
            mid = (lowerbound + upperbound) // 2
            if nums[mid] < 0:
                lowerbound = mid + 1
            else:
                upperbound = mid
        negative_count = lowerbound

        lowerbound = 0
        upperbound = len(nums)
        while lowerbound < upperbound:
            mid = (lowerbound + upperbound) // 2
            if nums[mid] <= 0:
                lowerbound = mid + 1
            else:
                upperbound = mid
        positive_count = len(nums) - lowerbound

        return max(negative_count, positive_count)

# Although we can do this problem with just a simple for loop:
#     negative_count = 0
#     positive_count = 0
#
#     for x in nums:
#         if x < 0:
#             negative_count += 1
#         elif x > 0:
#             positive_count += 1
#
#     return max(negative_count, positive_count)
# However, that is O(n) of time. Since binary searches are O(log n) and doing 2 would just be O(2log n), the constant would be ignored and
# ultimately it would be faster than O(n).
# Therefore, we'll conduct one binary search for negatives, one for the positives. For the negatives if the mid element is less than 0,
# then we just need to search in the upper half. The reason for this is because, if the mid element is greater than 0 or equal to 0 then we
# can just declare the upperbound as the mid. Once we bring our lowerbound to the exact place where positives and negatives separate, we can
# just declare the negative_count equal to the lowerbound.
# So imagine an array [-3,-2,-1,0,0,1,2]
# mid will land on the first 0, right after -1. Therefore, we can just make the mid our upperbound. Now we'll check between -3,-2,-1,0.
# The next mid would be -2. Since this is negative, we'll increment the lowerbound again to mid + 1. -1 becomes our next lowerbound. With one
# more check, the loop will conclude with lowerbound reaching 0, which happens to be our upperbound from before too. Therefore, the loop will
# exit with lowerbound being 3. Therefore, we can just declare our negative_count until 3 because our lowerbound will always end on either
# 0 or a positive value, so assigning that to negative_count will always give us the total for negatives.
# We can just simply apply this same boundary rule to positive_count, only this time, instead of declaring lowerbound as our negative_count,
# we can just declare our positives as the subtraction between the entire array and our lowerbound, since our lowerbound will always be
# either a 0 or a negative in this loop. Afterwards, we will return whichever count is bigger, so we'll just use a simple max function.