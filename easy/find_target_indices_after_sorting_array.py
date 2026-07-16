class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        result_array = []

        for i in range(0, len(nums)):
            for j in range(0, len(nums)-1):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp

        upperbound = len(nums)-1
        lowerbound = 0

        while lowerbound <= upperbound:
            mid = (lowerbound + upperbound)//2

            if nums[mid] == target:
                result_array.append(mid)
                left = mid-1
                right = mid+1
                while left >= 0 and nums[left] == target:
                    result_array.append(left)
                    left -= 1
                while right <= len(nums)-1 and nums[right] == target:
                    result_array.append(right)
                    right += 1
                break
            elif nums[mid] > target:
                upperbound = mid - 1
            elif nums[mid] < target:
                lowerbound = mid + 1

        return sorted(result_array)

# Firstly, we have to sort the array using a basic bubblesort.
# Then we need a conduct a binary search. The 3 cases are, if the mid element is bigger or smaller or equal to the target. The bigger or the
# smaller cases are very easy to deal with since we can just change the bounds.
# The case where it's equal to the target is the issue. This is because elements around it can also be the same as it is, but our mid just
# happens to land on a particular one.
# Therefore, then we need to declare two pointers, one going left, and the other going to right.
# We'll keep incrementing these pointers as long as they stay within the length of our array and as long as the elements these are at are
# equal to the target. We'll also append each of these alongside the mid itself to a result_array. Before returning, we need to sort the array
# since the question asks us to return the list sorted in increasing order.