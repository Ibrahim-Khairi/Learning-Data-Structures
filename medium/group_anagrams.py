class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        d = {}
        for word in strs:
            list = []

            for x in range(0, len(word)):
                list.append(word[x])

            for x in range(0, len(word)):
                for y in range(0, len(word)):
                    if list[x] < list[y]:
                        temp = list[x]
                        list[x] = list[y]
                        list[y] = temp

            key = ""

            for x in range(0, len(word)):
                key += list[x]

            if key not in d:
                d[key] = []
            d[key].append(word)

        list = []
        for value in d.values():
            list.append(value)

        return list

# So, at first I tried to figure out an anagram logic.
# A word is an anagram if it has the same amount of the same letters in any order.
# Therefore, to first see whether a word is an anagram, we need to figure out if they have the same length.
# Then we can take a letter from one word, and see if it's in the other. We can do this for the entire length.
# If every single is found and similar in both words then it means it is an anagram.
# word1 = "tan"
# word2 = "nat"
# letter_found = True
# if len(word1) == len(word2):
#     x = 0
#     while letter_found and x < len(word1):
#         if word1[x] in word2:
#             letter_found = True
#         else:
#             letter_found = False
#             break
#         x += 1
# else:
#     letter_found = False
#
# if letter_found:
#     print("anagram")
# else:
#     print("not anagram")
# Then, we need moved on to the entire array. Firstly, we had to figure out how to sort them length-wise and then letter-wise.
# To sort them by length of each word, we can just use a basic bubblesort algorithm.
# Next, we can iterate through the sorted array grouping each word of the same length words in an inner_array. The second we detect a
# length change, we can append the inner_array to the final_array.
# x = 1
# final_array = []
# inner_array = []
# inner_array.append(array[0])
# while x < len(array):
#     if len(array[x]) == len(array[x-1]):
#         inner_array.append(array[x])
#     else:
#         final_array.append(inner_array)
#         inner_array = []
#         inner_array.append(array[x])
#     x = x + 1
# final_array.append(inner_array)
#
# print(final_array)
# However, applying the anagram logic to the inner_array was getting very tedious. Therefore, I decided to go with dictionaries approach.
# Dictionaries are very simple. They have keys and values attached to them. One single key can have several values attached to it.
# So now, the question is, if anagrams have the same letters and the same amount of those letters, is there a simpler way of finding them?
# Sorting them alphabetically. word, dowr, rowd will all be sorted to dorw, when done alphabetically. Therefore, if we make dorw the key,
# and word, dowr, rowd the values attached to that key, we can actually get them grouped and sorted all together.
# So how to sort them alphabetically? Simple. We take each character from the word, and append it into an array. Then, we can just implement
# the bubblesorting algorithm to sort them. Finally, we can simply concatenate each of the element from that array to the key.
# If they key doesn't exist in dictionary, then we can initialize a new empty set with that key.
# Otherwise, we can just append the word to a key.