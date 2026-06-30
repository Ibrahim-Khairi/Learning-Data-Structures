class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """

        for row in image:
            left = 0
            right = len(row) - 1

            while left < right:
                temp = row[left]
                row[left] = row[right]
                row[right] = temp

                left += 1
                right -= 1

        for row in image:
            for x in range(0, len(row)):
                if row[x] == 0:
                    row[x] = 1
                elif row[x] == 1:
                    row[x] = 0

        return image

# First thing we do is reverse all rows.
# To do that, we just use the two pointer technique we learned to reverse in reverse_array.
# THen we need to flip all digits.
# Each 0 becomes 1, each 1 becomes 0. Simple selection statement suffices.