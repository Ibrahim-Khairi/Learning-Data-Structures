class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        count = 0

        for x in grid:
            lowerbound = 0
            upperbound = len(x) - 1

            while lowerbound <= upperbound:
                mid = (lowerbound + upperbound) // 2

                if x[mid] > 0:
                    lowerbound = mid + 1
                elif x[mid] < 0:
                    count = count + (upperbound - mid + 1)
                    upperbound = mid - 1
                elif x[mid] == 0:
                    lowerbound = mid + 1

        return count

# We'll iterate over each row of the grid, for that we'll declare a for loop that goes through every single row.
# We'll conduct a binary search in that specific row using a simple boundary method. If the mid element is greater than 0, then we know
# everything after it is to be checked. Everything before it would simply either be 0 or positive elements because each row is sorted in
# decreasing order.
# If the mid element happens to be less than 0, then we just need to check everything behind the mid. This is because we already know
# everything in front of it is in negatives because 0 is bigger than negatives and the mid element is already negative. So we can just
# add all the negative elements in front of the mid element to the count. We can do that through upperbound - mid + 1, the + 1 is to include
# the mid itself.
# If the mid element is 0 itself, then we just need to check the upper half of the array because everything before it is either positive or
# 0.