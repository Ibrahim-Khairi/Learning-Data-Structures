class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        while m > 0 or n > 0:
            if m == 0:
                nums1[m + n - 1] = nums2[n - 1]
                n = n - 1
            elif n == 0:
                break
            else:
                if nums1[m - 1] > nums2[n - 1]:
                    nums1[m + n - 1] = nums1[m - 1]
                    m = m - 1
                elif nums1[m - 1] < nums2[n - 1]:
                    nums1[m + n - 1] = nums2[n - 1]
                    n = n - 1
                else:
                    nums1[m + n - 1] = nums2[n - 1]
                    n = n - 1

        return nums1

# Both num arrays are sorted. Therefore, comparing the biggest one from each of these num arrays gives us the biggest number overall.
# Which means this can go at the end of num1. So, we need 3 pointers.
# Pointer 1 looks at the last element of num1. Pointer 2 looks at the last element of num2.
# We need these two pointers for comparison. The bigger of these two pointers will be used.
# Pointer 3 looks at the last position of num1 which is a non-element.
# So in [1,2,3,0,0,0] pt. 1 becomes num1[2] and pt. 3 becomes num1[5].
# And in [2,5,6] pt.2 becomes num1[2].
# Using m and n, we can say pt. 1 is num1[m-1], pt. 2 is num2[n-1], and pt. 3 is num1[m+n-1].
# In each iteration, we need to do these 3 things.
# 1) Compare pt. 1 and pt. 2.
# 2) Biggest one goes over to pt. 3.
# 3) Decrease m or n (whichever num array you take the bigger value from. m if you take from num1 (elements decrease) and n if you take
# from num2).
# The loop needs to go on while m and n are bigger than 0.
# However, there are three conditions.
# 1) m is bigger than 0 and n is 0.
# 2) n is bigger than 0 and m is 0.
# 3) both of them are bigger than 0.
# If they are both 0, we obviously will quit the loop.
# For condition 1, if n is 0, it means num2 is empty. Which means, the values in num1 are as is sorted and everything's merged, so we can
# just break the loop.
# For condition 2, if m is 0, it means there are no further elements in num1 left to compare. So, we can just put the entirety of num2 in
# num1's remaining non-element spots.
# Lastly, if they are both bigger than 0, we can just simply do the comparisons we talked about previously.
# God, this one required a bit of thinking man. I also tried a shifting algorithm which moves all the values to the right after a certain
# point. But that was getting too complicated and messy. Had to think of a two pointer approach just like we did in two sums to some extent.