class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        upperbound = len(nums) - 1
        lowerbound = 0
        found_flag = False
        mid = 0

        while lowerbound <= upperbound:
            mid = (lowerbound + upperbound) // 2

            if nums[mid] == target:
                found_flag = True
                break
            elif nums[mid] < target:
                lowerbound = mid + 1
            elif nums[mid] > target:
                upperbound = mid - 1

            if lowerbound >= upperbound:
                found_flag = False

        if found_flag:
            return mid
        else:
            return -1

# Fairly simple. Basically in binary search you have upperbound, lowerbound, and mid.
# mid helps you create two subsections in the array recurringly. if the target is found at mid, then we can just exit the loop otherwise
# we keep manipulating the bounds depending on which subsection of the array target lies in.