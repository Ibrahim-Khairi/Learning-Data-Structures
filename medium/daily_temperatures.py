class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        stack = []
        result_array = []

        for i in temperatures:
            result_array.append(0)

        for i in range(0, len(temperatures)):
            while len(stack) != 0 and temperatures[stack[len(stack)-1]] < temperatures[i]:
                resolved_index = stack.pop()
                result_array[resolved_index] = (i - resolved_index)
            stack.append(i)

        return result_array

# So we literally had to learn the monotonic stack concept for this problem. My first solution was something like this:
# result_array = []
# for x in range(0, len(temperatures)-1):
#     if temperatures[x] < temperatures[x+1]:
#         result_array.append(1)
#     else:
#         greater_found = False
#         for y in range(x+1, len(temperatures)):
#             if temperatures[x] < temperatures[y]:
#                 result_array.append(y-x)
#                 greater_found = True
#                 break
#         if not greater_found:
#             result_array.append(0)
# result_array.append(0)
# The idea was, we first see if the next day in temperatures is bigger than our current day, which would mean just one.
# In case it's not bigger, we can just keep a flag that would then continue to find what is the next biggest.
# This was more of a brute force solution, but it wasn't working when there wasn't a day bigger than one even when the temperatures array
# ended. Therefore, I resorted to learning monotonic stack that forces us to stay sorted, either always increasing or decreasing from bottom
# to top. Basically, you pop off anything that breaks the order before you push something new. And whatever you have pushed, it's gone
# permanently. This is because we've learned the answer about it, so in a way it's resolved. Usually works the best with nearest element
# problems.
# So first, we need to make a result_array full of 0s for each corresponding day, as that day's answer for the time being. We'll later
# adjust these.
# Then, we need to iterate through each day in the temperatures array. If the stack is empty, we'll just directly push the first day's index
# in. Otherwise, we'll see whether the current day is greater than the day at the top of the stack. If it is then we have resolved the
# top day in the stack. We'll pop it out, store the distance between the iterative variable and the resolved day's index in the same index
# in result_array. After that, we can just simply get out of the loop and push that index in.
# Here, our stack is built up of INDICES, not VALUES. To access values we NEED to do temperature[(stack_index or whatever)].