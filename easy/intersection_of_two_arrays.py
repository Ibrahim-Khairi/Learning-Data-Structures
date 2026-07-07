class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        intersection = []
        freq = {}
        if len(nums1) > len(nums2):
            for num in nums1:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
        elif len(nums2) > len(nums1):
            for num in nums2:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
        else:
            for num in nums1:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1

        for key in freq:
            if key in nums1 and key in nums2:
                intersection.append(key)

        return intersection

# We just make a frequency map for the array with more elements in it. This is because the intersection can at most be the number of
# elements in the smaller array, so the larger array is basically a superset of it, if that makes sense.
# Then we simply see if each key in that frequency map exists in both the arrays, if it does that's an intersection.