class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        writer_pointer = 1
        for reader_pointer in range(1, len(nums)):
            if nums[reader_pointer] != nums[writer_pointer - 1]:
                nums[writer_pointer] = nums[reader_pointer]
                writer_pointer += 1
        return writer_pointer

# there is a writer pointer and a reader pointer.
# the writer pointer stays until the reader point has detected a unique number.
# upon detection, the writer pointer writes that number there.
# visual representation:
# [1, 1, 1, 2, 2, 3, 4, 4, 5]
# now writer stays at [1,
# reader starts from 1 (1st index), keeps reading. it finds 2.
# writer writes [1, 2,
# reader then continues, keeps reading. it finds 3.
# writer writes [1, 2, 3,
# reader finds 4.
# writer writes [1, 2, 3, 4,
# reader finds 5.
# writer writes [1, 2, 3, 4, 5,
# since leetcode only reads till k, if we return the writer_pointer (the amount of unique numbers), we don't need to care about the rest of the numbers.