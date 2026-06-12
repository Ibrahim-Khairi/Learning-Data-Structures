class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # if len(s) == len(t):
        #     list_s = []
        #     list_t = []
        #     for x in range(0, len(s)):
        #         list_s.append(s[x])
        #         list_t.append(t[x])
        #
        #     for x in range(0, len(s)):
        #         for y in range(0, len(s)):
        #             if list_s[x] < list_s[y]:
        #                 temp = list_s[x]
        #                 list_s[x] = list_s[y]
        #                 list_s[y] = temp
        #             if list_t[x] < list_t[y]:
        #                 temp = list_t[x]
        #                 list_t[x] = list_t[y]
        #                 list_t[y] = temp
        #
        #     if list_s == list_t:
        #         return True
        #     else:
        #         return False
        # else:
        #     return False

        if len(s) == len(t):
            freq_s = {}
            freq_t = {}

            for char in s:
                if char in freq_s:
                    freq_s[char] += 1
                else:
                    freq_s[char] = 1
            for char in t:
                if char in freq_t:
                    freq_t[char] += 1
                else:
                    freq_t[char] = 1

            return freq_s == freq_t

        else:
            return False

# We'll just simply apply a frequency mapping algorithm.
# If the length, isn't equal, then it's not an anagram as it is.
# In this, we'll first build around the frequency maps for each of the word.
# Then, we'll just compare the frequency maps. If they are the same, it means it is an anagram.
# Order does not matter for dictionary equality.
