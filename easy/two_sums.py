class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for x in range(0, len(nums)):
            for y in range(x+1, len(nums)):
                if nums[y] + nums[x] == target:
                    return x,y
        return None

# x is the base pointer.
# y is the inner pointer. it does all the comparisons with x.