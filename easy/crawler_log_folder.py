class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """

        folder = []

        for x in range(0, len(logs)):
            if len(folder) == 0:
                if logs[x] != "./" and logs[x] != "../":
                    folder.append(logs[x])
                else:
                    continue
            else:
                if logs[x] == "../":
                    if len(folder) == 0:
                        continue
                    else:
                        folder.pop()
                elif logs[x] == "./":
                    continue
                else:
                    folder.append(logs[x])

        return len(folder)

# There's three conditions.
# 1) ../ -> Go back to parent folder. Meaning, pop the element at the top of the folder stack.
# 2) ./ -> Do literally nothing.
# 3) x/ -> Push an element in the folder stack.
# Firstly, if there's nothing in the folder stack then we need to append something in it. To do that we check whether that is either "./" or
# "../". If it's neither of those, that means it's a regular folder, therefore, we can return it.
# After that, we can just check for the conditions as normal.