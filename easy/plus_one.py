class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return_array = []
        input = ""
        for digit in digits:
            input += str(digit)

        input = int(input) + 1
        input = str(input)

        for num in input:
            return_array.append(int(num))

        return return_array

# take each digit, convert it into char/string, add it into a string.
# convert the string into an integer, add one.
# take the calculated integer, convert it into a string back.
# iterate through each character/digit in the string, convert it back into an integer, and append it to the return_array.