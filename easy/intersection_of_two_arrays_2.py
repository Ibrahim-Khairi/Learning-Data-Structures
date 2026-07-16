class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result_array = []

        freq_1 = {}
        freq_2 = {}

        for x in nums1:
            if x not in freq_1:
                freq_1[x] = 1
            else:
                freq_1[x] += 1

        for y in nums2:
            if y not in freq_2:
                freq_2[y] = 1
            else:
                freq_2[y] += 1

        for key in freq_1:
            if key in freq_2:
                for z in range(0, min(freq_1[key], freq_2[key])):
                    result_array.append(key)

        return result_array

# We draw up frequency maps for each of the num arrays.
# Then we initialize a loop for freq_1 and check if that key we're iterating over exists in freq_2. If it does, then we'll append that key
# in the result array as many times as the lowest frequency of it exists in both the frequency maps. The reason we take the min is because,
# the lower amount is the intersection.
# So if num1 has [1,2,2] and num3 has [2,3], then the intersection is just the 2 in num3. So we take the minimum frequency.