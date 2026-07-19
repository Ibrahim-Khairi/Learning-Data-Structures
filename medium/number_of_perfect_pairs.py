class Solution(object):
    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if abs(left[i]) < abs(right[j]):
                result.append(abs(left[i]))
                i += 1
            else:
                result.append(abs(right[j]))
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr)//2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        sortedLeft = self.mergeSort(leftHalf)
        sortedRight = self.mergeSort(rightHalf)

        return self.merge(sortedLeft, sortedRight)

    def perfectPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        perfect_pairs = 0

        nums = self.mergeSort(nums)

        y = 1
        for x in range(0, len(nums)):
            while y < len(nums) and abs(nums[y]) <= 2*abs(nums[x]):
                y += 1
            perfect_pairs += y-x-1

        return perfect_pairs

# Initially, I tried a double nested solution which exceeded the time limit:
# for x in range(0, len(nums)-1):
#     for y in range(x+1, len(nums)):
#         a = nums[x]
#         b = nums[y]
#         if min(abs(a-b), abs(a+b)) <= min(abs(a), abs(b)) and max(abs(a-b), abs(a+b)) >= max(abs(a), abs(b)):
#             perfect_pairs += 1
# Therefore, we had to improvise an O(n) solution. We learnt that we can have a while loop inside a for loop if the pointer only ever goes
# forward and remains within the length of an array. It isn't restarting back from 0 or 1 or whatever. It's just going forward.
# The first thing we need to do is sort the array according to their absolute values. We need to do this in order to check incrementing pairs.
# So like the array [0,1,2,3] is sorted already in terms of absolute values - therefore we can check:
# 1) 0,1 -> 0,2 -> 0,3 (doesnt work)
# 2) 1,2 -> 1,3 (1,2 works only)
# 3) 2,3 (2,3 works)
# Since we have established the fact we need sorted arrays, we can just use a merge sort on this. We'll have two pointers - an x pointer that
# iterates from 0->len(nums)-1, and y pointer that iterates from 1->len(nums) only upon the fulfillment of a certain condition. Since the y loop
# is already initialized outside the y loop, it won't be restarting every single time from 1.
# The condition min(|a - b|, |a + b|) <= min(|a|, |b|) and max(|a - b|, |a + b|) >= max(|a|, |b|) can further be written as y <= 2x and x >= 0.
# min(|a-b|, |a+b|) = y - x
# max(|a-b|, |a+b|) = y + x
# min(|a|, |b|) = x
# max(|a|, |b|) = y
# Let's test all these for a testcase x = |1|, y = |-2| -> a = 1, b = -2
# 1) min(|1+2|, |1-2|) -> 3,1 -> 1    (2-1=1)
# 2) max(|1+2|, |1-2|) -> 3,1 -> 3    (2+1=3)
# 3) min(|1|, |-2|) -> 1,2 -> 1       (1)
# 4) max(|1|, |-2|) -> 1,2 -> 2       (2)
# Therefore, min(|a-b|, |a+b|) <= min(|a|, |b|) becomes y - x <= x -> y <= 2x.
# Similarly, max(|a-b|, |a+b|) >= max(|a|, |b|) becomes y + x >= y -> x >= 0
# Now that we have those two conditions, we can apply them. x simply becomes a for loop 0->len(nums) whereas y becomes a while loop starting from 1
# until right before len(nums) with the condition y <= 2x which can just simply be written as abs(nums[y]) <= 2*abs(nums[x]). While both of these
# conditions are fulfilled, we'll keep advancing y. At this point, every index between x+1 and y-1 forms a valid perfect pair with x.
# After we quit the while loop, we'll just increment the perfect pair by (y+1) - (y-1) + 1 (to keep that last value into consideration as well).
# This ultimately simplifies to y-x-1.
# By the way, this was one of the questions I was asked in an interview by Visa.