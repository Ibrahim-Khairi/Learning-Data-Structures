class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        left = 0
        right = len(s) - 1

        while left <= right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1

        return s

# Heads up, I did this so I could do rotate_array.
# At first, I tried a stack solution:
# stack = []
# x = len(string)-1
# while x >= 0:
#     result = string.pop()
#     stack.append(result)
#     x -= 1
# But then I realized the question says "You must do this by modifying the input array in-place with O(1) extra memory".
# Therefore, I looked at it, I searched up a video for it cause initially I was doing something like for x in range(0, len(s)//2): for some
# reason. Anyhow, I found a NeetCode video saying you take the first element, put it on last. You take the last element, put it on first.
# Through basic bubble-sorting, you know how to temporarily store a value that you're going to change, only to later place it elsewhere.
# After that I just knew it was a two-pointer problem, and we just need to keep moving inwards.
# Best believe now we are NEVER getting stuck in reversing shit.