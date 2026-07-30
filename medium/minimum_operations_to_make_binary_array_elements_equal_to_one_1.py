class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        minimum_operations = 0

        left = 0
        for right in range(2, len(nums)):
            if right-left+1 == 3:
                if nums[left] == 0:
                    nums[left] = 1
                    if nums[left+1] == 0:
                        nums[left+1] = 1
                    else:
                        nums[left+1] = 0
                    if nums[right] == 0:
                        nums[right] = 1
                    else:
                        nums[right] = 0
                    minimum_operations += 1
            left += 1

        if nums[-1] == 0 or nums[-2] == 0 or nums[-3] == 0:
            return -1

        return minimum_operations

# We declare the minimum_operations count to be returned, and the left pointer.
# Then we run a for loop, from 2. This is because we need a fixed-sized window of 3. Therefore, we'll check if the window's length (right-left+1)
# is equal to 3, and then we'll check if the left-most element is a 0, which means it's an unresolved zero which is the first to be fixed before
# moving the sliding window onwards. Then we'll just flip if every other element through basic if structures. And since that is an unresolved zero,
# we will also be adding incrementing the minimum_operations counter by 1 since that's already a flip registered.
# At the end we'll check if any of the last 3 elements have a 0, if they do, that means it was impossible to make all elements one, therefore,
# we'll just return -1.