class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            if area > max_area:
                max_area = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# So, at first a tried a double nested approach that will basically compare each line with every other line and find out the max area as per
# that. While that works, it's not appropriate for extremely large input sizes because of its O(n^2) complexity. And that's exactly what
# happened, I failed a testcase because the time limit exceeded. Here's the solution for that:
#     for x in range(0,len(height)):
#         for y in range(0,len(height)):
#             if height[x]<height[y]:
#                 area_height = height[x]
#                 area_base = y-x
#                 area = area_height * area_base
#                 if area > max_area:
#                     max_area = area
#             elif height[y]<height[x]:
#                 area_height = height[y]
#                 area_base = y-x
#                 area = area_height * area_base
#                 if area > max_area:
#                     max_area = area
#             elif height[x]==height[y]:
#                 area_height = height[x]
#                 area_base = y-x
#                 area = area_height * area_base
#                 if area > max_area:
#                     max_area = area
# Therefore, I then tried a two pointer approach. We will check the left pointer with the right pointer. Ofcourse we know the area's height
# will be the shorter one because the larger one encapsulates the smaller one, and so the water will not flow out. For the area's base, we
# know it's right-left. Right is the bigger one, therefore we subtract left from right. Question is, why subtract at all? Because We need
# to find the area between those two lines. If right is 4, and left is 2, the area would be between these, meaning 2. If we just do right,
# it will take from the origin quite literally.
# Now the problem arises when we have to decide which pointer to move inwards. We resolve this by finding out which pointer has a smaller
# height. If we were to move the taller one's pointer inside, it would mean we might just get lesser height coupled with lesser width.
# If we were to move the shorter one's pointer inside, it would mean we might just get bigger height even if we are still getting lesser
# width. Therefore, we move the pointer inside for whichever one's smaller.