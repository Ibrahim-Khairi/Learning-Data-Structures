class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        record = []

        for x in range(0, len(operations)):
            if operations[x] == "C":
                record.pop()
            elif operations[x] == "D":
                record.append(record[len(record) - 1] * 2)
            elif operations[x] == "+":
                num_1 = record[len(record) - 1]
                num_2 = record[len(record) - 2]
                record.append(num_1 + num_2)
            else:
                record.append(int(operations[x]))

        sum = 0
        for x in range(0, len(record)):
            sum += record[x]

        return sum

# Literally the only thing that's worthy explaining in this problem is len(record) - 1 gives you the last element because len(record) means
# the number of elements and subtracting 1 from it gives you the last element index. Similarly, len(record) - 2 gives you the second last
# element which is what we need for the "+" operation.