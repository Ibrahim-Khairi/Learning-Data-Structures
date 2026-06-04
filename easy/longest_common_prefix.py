class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        return_array = strs[0]
        for strings in range(1, len(strs)):
            for letter_pointer in range(min(len(return_array), len(strs[strings]))):
                if return_array[letter_pointer] != strs[strings][letter_pointer]:
                    return_array = return_array[:letter_pointer]
                    break
            return_array = return_array[:len(strs[strings])]
        return return_array

# we make return_array the base array to base all our comparisons off of. hence, it's the first string.
# then, we are going to iterate through the entire array and get every string.
# then, there's going to be a letter_pointer that runs through the strings. it needs to run for the duration of the minimum
# of the return_array and the current string. so let's say flower and flow. we will run for 4 letters of flow, because that's the maximum
# possible similarity they can have, since flow does not have e and r.
# now we are going to see if the letters are similar or not. the second they are not similar, we slice the return_array and immediately
# break the loop since we have no other conditions to check afterwards.

string = ["ab, a"]
case = Solution()
print(case.longestCommonPrefix(string))