class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        answer = []

        left = 0
        freq_map = {}
        for right in range(len(nums)):
            freq_map[nums[right]] = freq_map.get(nums[right], 0) + 1
            if right-left+1 == k:
                sorted_items = sorted(freq_map.items(), key=lambda item: (item[1], item[0]), reverse=True)
                x_sum = 0
                for i in range(min(x, len(sorted_items))):
                    key, freq = sorted_items[i]
                    x_sum += key * freq
                answer.append(x_sum)
                freq_map[nums[left]] = freq_map.get(nums[left], 0) - 1
                left += 1

        return answer

# We'll initialize the answer array to be returned, the left pointer and the freq_map.
# We'll iterate right from 0->len(nums) and append each character on the right to the freq_map if it exists, otherwise initializes it.
# Then we check whether the window size is exactly k. If it is, then first we'll sort the freq_map.
# To do that, we'll use sorted(freq_map.items(), key=lambda item: (item[1], item[0]), reverse=True).
# 1) freq_map.items() turns dictionary into a list of tuples of key, value.
# 2) the lamba function, item[1] refers to the value and item[0] refers to the value in the tuple.
# 3) reverse=True sorts in descending order.
# -> doing sorted(x.items(), key=lambda item: item[1]) sorts the dictionary items in ascending order based strictly on their values. Since we are
# only looking at the values, we are sorting them by frequencies, so basically least-frequent -> most-frequent.
# -> doing sorted(x.items(), key=lambda item: (item[1], item[0])) sorts the dictionary items by value first, and then breaks the ties by value of
# the key itself.
# -> doing sorted(freq_map.items(), key=lambda item: (item[1], item[0]), reverse=True) sorts the dictionary items by value first in descending
# order, and then breaks the ties by value of the key itself in descending order.
# So in an array [1,1,2,2,3,4], it would give the freq_map as {1: 2, 2: 2, 3: 1, 4: 1}.
# Then doing freq_map.items() would give a list of tuples with key, value pairs [(1, 2), (2, 2), (3, 1), (4, 1)].
# Then doing item[1], would sort them by value from least-frequent to most-frequent [(3, 1), (4, 1), (1, 2), (2, 2)].
# Adding item[0] to it, would sort ties of equal frequency by the value of the key (least->most) [(3, 1), (4, 1), (1, 2), (2, 2)].
# Then doing reverse=True, would do everything from most->least [(2, 2), (1, 2), (4, 1), (3, 1)].
# Now, we can just initialize x_sum and loop through the sorted_items, destructuring the tuple to key, value.
# We then just add key * freq to the x_sum. So if there's (2,2), we need to add 2, 2 times. Therefore, 2 * 2 would just give 4.
# Once we are done iterating through the entire list, we can just append the x_sum to the answer for that sliding window.
# We can then just increment the left pointer at the very end.