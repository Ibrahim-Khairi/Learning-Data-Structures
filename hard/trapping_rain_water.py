class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_left = [0] * len(height)
        max_right = [0] * len(height)

        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i-1])

        for i in range(len(height)-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])

        water_level = 0

        for i in range(0, len(height)):
            min_between_walls = min(max_left[i], max_right[i])
            if min_between_walls > height[i]:
                water_level += min_between_walls - height[i]

        return water_level

# THIS WAS MY FIRST HARD PROBLEM. YAYYYYY!
# So at first, I tried a monotonic stack approach where I got the greater wall to the right and to the left:
# water_levels_to_right = [0] * len(height)
# stack = []
#
# for i in range(len(height)):
#     while stack and height[stack[-1]] < height[i]:
#         resolved_index = stack.pop()
#         water_levels_to_right[resolved_index] = height[i]
#     stack.append(i)
#
# water_levels_to_left = [0] * len(height)
# stack = []
# for i in range(len(height)-1, -1, -1):
#     while stack and height[stack[-1]] < height[i]:
#         resolved_index = stack.pop()
#         water_levels_to_left[resolved_index] = height[i]
#     stack.append(i)
#
# water_level = 0
#
# for i in range(0, len(water_levels_to_right)):
#     min_between_walls = min(water_levels_to_right[i], water_levels_to_left[i])
#     water_level += height[i] - min_between_walls
#
# return water_level
# However, the problem between this was, it wasn't taking the MAXIMUM wall, only the greater element to the left and to the right. Now the
# question is - why do we need the maximum walls? This is something that you deduce from the picture that they've given you, or rationale,
# I guess. Basically, the maximum wall to the left and to the right give you the "highest possible" level that the water could achieve.
# Then taking the minimum of those heights, gives us the actual achieveable height.
# For example, if we see the [0,1,0,2,1,0,1,3,2,1,2,1] array.
#                                |"""|
#                                |___|
#            |"""|~~~~~~~~~~~~~~~|"""||"""|~~~~~|"""|
#            |___|               |___||___|     |___|
#  |"""|~~~~~|"""||"""|~~~~~|"""||"""||"""||"""||"""||"""|
#  |___|     |___||___|     |___||___||___||___||___||___|
# For the [-3] value or the second last "1", the maximum wall to it's left is [-5] or "3". This means, it's the highest possible level that
# it could possibly achieve, without taking into consideration what the maximum wall towards the right is. Then, we find the maximum wall to
# the right being [-2] or "2". The minimum of these two walls is basically the level that we could achieve. Now how do we calculate the water
# level? We basically need to minus the height of the element that we are iterating over itself. The reason for that is, it's kind of like a
# pothole. If the [-3] value was 0 instead of 1, then it would be like:
#                                |"""|
#                                |___|
#            |"""|~~~~~~~~~~~~~~~|"""||"""|~~~~~|"""|
#            |___|               |___||___|     |___|
#  |"""|~~~~~|"""||"""|~~~~~|"""||"""||"""|~~~~~|"""||"""|
#  |___|     |___||___|     |___||___||___||___||___||___|
# Therefore, to get the actual water level, we just need to subtract the height from the minimum of the maximum tallest walls towards the left
# and towards the right.