class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """

        window_dict = {"T":0, "F":0}
        left = right = 0
        for right in range(len(answerKey)):
            window_dict[answerKey[right]] += 1
            max_count = max(window_dict.values())
            if right-left+1-max_count > k:
                window_dict[answerKey[left]] -= 1
                if window_dict[answerKey[left]] == 0:
                    window_dict.pop(answerKey[left])
                left += 1

        return right-left+1

# We'll initialize the two pointers and a window_dict for T and F. At the start, these are both going to have 0 as their values.
# At each right's iteration, we'll add 1 to the frequency for it.
# We'll then check which value is more - T or F. Accordingly, we'll store that in a variable that we will deduct from the length of the window to
# see if it's greater than the amount of operations we can make. If it is, then we just increment left, making changes to its frequency.
# So imagine "FFFTTFTTFT" with k=3.
# We'll keep checking the entire window.
# right = 1, left = 0, {F:1, T:0}, max_count = 1, window_length = 2
# right = 0, left = 0, {F:2, T:0}, max_count = 2, window_length = 1
# right = 2, left = 0, {F:3, T:0}, max_count = 3, window_length = 3
# right = 3, left = 0, {F:3, T:1}, max_count = 3, window_length = 4
# right = 4, left = 0, {F:3, T:2}, max_count = 3, window_length = 5
# right = 5, left = 0, {F:4, T:2}, max_count = 4, window_length = 6
# right = 6, left = 0, {F:4, T:3}, max_count = 4, window_length = 7
# right = 7, left = 0, {F:4, T:4}, max_count = 4, window_length = 8 => 8-4 > k, increment left. left = 1, {F:3, T:4}.
# right = 8, left = 1, {F:4, T:4}, max_count = 4, window_length = 8 => 8-4 > k, increment left. left = 2, {F:3, T:4}.
# right = 9, left = 2, {F:3, T:5}, max_count = 5, window_length = 8
# Then we just return the window_length which is 8, so the final post-changes exam should look like "FFTTTTTTTT".