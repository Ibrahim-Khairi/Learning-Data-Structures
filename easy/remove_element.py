class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        writer_pointer = 0
        for reader_pointer in range(0, len(nums)):
            if nums[reader_pointer] != val:
                nums[writer_pointer] = nums[reader_pointer]
                writer_pointer += 1

        return writer_pointer

# quite literally the same thing as Longest Common Prefix except this time it's easier because we have to compare it with a given value