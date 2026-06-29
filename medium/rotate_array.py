class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        left = 0
        right = len(nums)-1

        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1

        left = 0
        right = k-1
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1

        left = k
        right = len(nums)-1
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1

# Heads up, I did this so I could do rotate_list.
# This took an unusually long amount of time.
# I made a lot of solutions for this, which are honestly quite complex to explain, so I'll just copy-paste them here to save time without
# explaining why I did them. However, I will be explaining my logic behind the second-last solution.
# First solution:
# temp_nums = []
# for x in nums:
#     temp_nums.append(0)
# y = k
# while y <= len(temp_nums)-1:
#     temp_nums[y] = nums[y-k]
#     y += 1
# z = 0
# while z < k:
#     temp_nums[z] = nums[z-k]
#     z += 1
# return nums
# Didn't work because we need to modify nums itself.
# Second solution:
# temp_nums = []
# for a in nums:
#     temp_nums.append(a)
#
# temp = nums[k]
#
# for x in range(k, len(nums)):
#     nums[x] = nums[x-k]
#
# nums[-1] = temp
#
# for y in range(0, len(temp_nums)//2):
#     nums[y] = temp_nums[-(y+1)]
#
# rotate_nums = []
#
# for z in range(0, k):
#     rotate_nums.append(nums[z])
#
# pointer = 0
# while pointer < k:
#     nums[pointer] = rotate_nums[(-pointer+k-1)]
#     pointer += 1
#
# print(nums)
# Here, I figured out we are supposed to do some rotations. But since I actually didn't even know how to rotate with two pointers, it got
# unnecessarily complex, long, and didn't even work.
# Third solution:
# left = 0
# right = len(nums)-1
#
# if k > 0:
#     if right > 0 and len(nums) > 2:
#         while left < right:
#             temp = nums[left]
#             nums[left] = nums[right]
#             nums[right] = temp
#             left += 1
#             right -= 1
#
#         left = 0
#         right = k-1
#         while left < right:
#             temp = nums[left]
#             nums[left] = nums[right]
#             nums[right] = temp
#             left += 1
#             right -= 1
#
#         left = k
#         right = len(nums)-1
#         while left < right:
#             temp = nums[left]
#             nums[left] = nums[right]
#             nums[right] = temp
#             left += 1
#             right -= 1
#     else:
#         if k % 2 == 0:
#             left = 0
#             right = len(nums)-1
#             while left < right:
#                 temp = nums[left]
#                 nums[left] = nums[right]
#                 nums[right] = temp
#                 left += 1
#                 right -= 1
# This is where I cracked the reversal building up on reverse_string. However, I kept failing on particular test-cases. The k was always
# messing me up. It was either 0, 1, 2, sometimes even more than the length of array itself.
# Therefore, we needed to find a way to remove the extra trips. if we got nums [2,1] and k was 2, it would become [1,2] and land back to
# [2,1]. Then, even if k was something like 24, it would still do that. Getting the modulus of len(nums)/k gives us the actual amount of
# rotations that are actually even worthwhile. Thereafter, I just had to apply the reversal that I used in the third solution.