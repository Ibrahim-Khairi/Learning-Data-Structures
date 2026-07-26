class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """

        subarray_count = 0
        window_sum = sum(arr[0:k])
        window_avg =  window_sum/float(k)

        subarray_count += 1 if window_avg >= threshold else 0

        left = 0
        for right in range(k, len(arr)):
            window_sum += arr[right]
            window_sum -= arr[left]
            left += 1
            if right-left+1 == k:
                window_avg = window_sum/float(k)
                if window_avg >= threshold:
                    subarray_count += 1

        return subarray_count

# This is a fixed-window problem, so it is fairly simple.
# We'll first declare a subarray_count counter variable to be returned.
# Then we'll calculate the sum of all the elements from 0->k (excluded, since that will be accounted for later). With the help of this sum, we'll
# derive the initial window_avg dividing it by float(k).
# We'll then check if that window_avg is greater than or equal to the threshold and update the subarray_count accordingly.
# We'll then enter the main loop, iterating right from l->len(array)-1. The left pointer initialized before helps us check the window size. At
# each iteration, we'll add the right pointer's element to the window_sum, and remove the left pointer's element from the window_sum.
# We'll then increment the left pointer, and check whether the window size (right-left+1) is equal to k. If it is, then we'll simply calculate the
# new window_avg, and compare it against threshold, incrementing the subarray_count counter variable accordingly.