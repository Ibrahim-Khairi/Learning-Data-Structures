class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        for i in range(0, len(arr)):
            for j in range(0, len(arr)-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp

        for x in range(0, len(arr)):
            upperbound = len(arr)-1
            lowerbound = 0

            while lowerbound <= upperbound:
                mid = (upperbound+lowerbound)//2
                if arr[x] * 2 == arr[mid] and x != mid:
                    return True
                elif arr[x] * 2 == arr[mid]:
                    upperbound = mid - 1
                elif arr[x] * 2 < arr[mid]:
                    upperbound = mid - 1
                elif arr[x] * 2 > arr[mid]:
                    lowerbound = mid + 1

        return False

# Firstly, we need to sort the array using a basic bubblesorting algorithm.
# Secondly, we need to conduct a binary search, where we need to see whether the specific element that we are iterating over times two is
# equal to mid or not, while also checking whether it doesn't share the same index as mid - for values such as 0 or 1.
# If it happens to share the same index, then we can just create the upperbound behind mid because the array is sorted and we know there's
# nothing after the mid that would equate to n or it's double.
# Otherwise, if the doubled number is less than mid, then we can just decrement the mid to be the upperbound - since it's in the lower half.
# And we do the vice versa if its greater than mid, because we know it's in the upper half of the array.