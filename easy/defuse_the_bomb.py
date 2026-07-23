class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """

        result_array = [0]*len(code)

        if k < 0:
            for right in range(0, (k*-1)):
                result_array[right] = sum(code[right+k:]+code[:right])
            for right in range((k*-1), len(code)):
                result_array[right] = sum(code[right+k:right])
        elif k > 0:
            for right in range(0, len(code)-k):
                result_array[right] = sum(code[right+1:right+k+1])
            for right in range(len(code)-k, len(code)):
                result_array[right] = sum(code[right+1:]+code[:k-len(code)+right+1])

        return result_array

print(Solution().decrypt([5,7,1,4], 3))

# We'll initially declare the result_array as an array sized at what the length of code is, with each element being initiated as 0.
# There's 3 cases that we need to deal with depending on what k is.
# If k is 0, then we don't need to do anything since the result_array already has 0s.
# In the case that k is negative, we first need to iterate from 0->k*-1. Then we need to basically get all the elements after right-k, and all
# the elements before right, since it's previous elements. We can then take a sum of all of these. Since we are doing code[right+k:]+code[:right]
# this basically goes in a circular way.
# Then, we need to deal with the lower half, so we iterate from k*-1 to len(code). Since this is the second half, we just need to get everything
# from right-k to right. k being negative does the job of right-k, and we already have right so we can just do right+k:right.
# So consider the array [2,4,9,3] and k = -2.
# For the upper half (2,4), we'll iterate from 0->2 (k*-1). 2 is excluded, so we are basically just doing index 0 and 1.
# For 2, we need the sum of 9+3. Our right is currently at 0, if we do get code[-2] and code[-1], it gets us 9 and 3. Therefore, we do right+k
# and all the elements that point on. This is because k is already negative so adding right to it would just make it right-k. The next part is
# getting everything before right, just in case. Since there's nothing towards the left of right here, we can just skip out on that.
# For 4, we need the sum of 3+2. So again we do right-k (k is 2, so 1-2 would give us -1). That covers the "circular-previous" part, and we get
# 3. Then, we just get everything before right, which in this case happens to be 2. Therefore, 3+2 gives us 5.
# For the lower half (9,3), we'll iterate from 2->len(nums). 4 is excluded, so we are basically just doing index 2 and 3.
# For 9, we need the sum of 2+4. Our right is currently at 2, so we just need everything between right+k and right. 2-2 gives us 0. 0:2 gives us
# nums[0] and nums[1]. The same goes for 3. right is at 3, 3-2 gives 1:3 (index 1 and 2).
# In the case that k is positive, we first need to iterate from 0->len(code)-k. This gives you the first half of the array or basically
# everything before our k window. Then we basically need to get everything after right all the way up until right-k+1 (the 1 accounts for the
# ending element too). right-k+1 gives us the left most pointer before the starting of the k window itself, and right+1 gives us everything after
# right itself.
# Afterwards, we run another for loop, this time from len(code)-k->len(code) itself. This is the actual k window. Here, we need to get everything
# after right, and then everything in the "circular" part. Everything after right can just be right+1:, and then we need the wrapping part.
# The amount of elements that go in the non-circular part or right+1 part is basically just len(code)-(right+1), equating to len(code)-right-1.
# Since we need k in total, the elements that we need from the front of the array are just k-(len(code)-(right+1)) which simplifies to
# k-len(code)+right+1.