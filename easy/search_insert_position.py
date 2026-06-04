class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        return_value = None
        for x in range(0, len(nums)):
            if nums[x] == target:
                return_value = x
                break
            elif x != len(nums) - 1 and nums[x] < target < nums[x + 1]:
                return_value = x + 1
                break
            elif nums[x] > target > nums[x - 1]:
                return_value = x - 1
                break
            elif target > nums[x]:
                return_value = len(nums)
            else:
                return_value = 0

        return return_value

# the first condition simply returns index if target spotted.
# the second condition sees if target is bigger than the current element, smaller than the next element, and hasn't reached
# the end of the array yet. Then it simply increments x, and says it'll be inserted right infront of it.
# the third condition sees if target is smaller than the current element, and bigger than the previous element. decrements x.
# the fourth condition sees if target is basically bigger than all the numbers in array, then it'll be inserted after the last
# element. Since we can't do len(nums)-1 because that'll trigger  we have to do len(nums).
# the fifth condition sees if target is smaller than the first element , then it just simply returns 0, meaning it should be in
# the first index.