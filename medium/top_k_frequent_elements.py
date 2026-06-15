class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        buckets = [[] for x in range(0, len(nums) + 1)]

        for key in freq:
            buckets[freq[key]].append(key)

        output_array = []
        count = 0
        for x in range(len(buckets)-1, 0, -1):
            if not buckets[x] == [] and count < k and len(buckets[x]) <= k:
                count += len(buckets[x])
                for y in range(0, len(buckets[x])):
                    output_array.append(buckets[x][y])

        return output_array

# My initial approach towards solving this problem was to build a simple frequency map, make two arrays appending each key and value.
# Then bubblesorting those from max to min, and finally outputting the keys as per the frequency/values.
# However, that failed the last testcase because the input was too large. Here's the solution for that:
#     max_to_min_frequency_key = []
#     max_to_min_frequency_value = []
#
#     for key in freq:
#         max_to_min_frequency_key.append(key)
#         max_to_min_frequency_value.append(freq[key])
#
#     for x in range(0, len(max_to_min_frequency_value)):
#         for y in range(0, len(max_to_min_frequency_value)):
#             if max_to_min_frequency_value[x] > max_to_min_frequency_value[y]:
#                 temp = max_to_min_frequency_value[x]
#                 temp2 = max_to_min_frequency_key[x]
#                 max_to_min_frequency_value[x] = max_to_min_frequency_value[y]
#                 max_to_min_frequency_key[x] = max_to_min_frequency_key[y]
#                 max_to_min_frequency_value[y] = temp
#                 max_to_min_frequency_key[y] = temp2
#
#     output_array = []
#     for x in range(0, k):
#         output_array.append(max_to_min_frequency_key[x])
#
#     return output_array
# Therefore, I resorted to learning and implementing bucket sort.
# Since the maximum possible frequency of any number is len(nums), meaning, if the entire nums array is just one number, we can create an
# array of len(nums) + 1 buckets, where index would represent frequency. As a result, we can just drop every number into its corresponding
# frequency bucket.
# Also, for the last codeblock where we are just reading backwards k many elements, we can also do a simpler version that actually solves
# more issues.
#     for x in range(len(buckets)-1, 0, -1):
#         for y in range(0, len(buckets[x])):
#             output_array.append(buckets[x][y])
#             if len(output_array) == k:
#                 return output_array
# In our code, len(buckets[x]) <= k, a bucket could have more elements than k, but we would still want to take some of the numbers from it.
# But yeah since this codeblock occurred to me after the solution was done, I didn't care to actually fix it. Oopsies.