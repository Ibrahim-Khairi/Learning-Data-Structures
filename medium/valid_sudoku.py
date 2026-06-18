class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        row_freq_map_array = []
        for row in range(0, len(board)):
            row_freq_map_dic = {}
            for x in range(0, len(board[row])):
                if board[row][x] != ".":
                    if board[row][x] not in row_freq_map_dic:
                        row_freq_map_dic[board[row][x]] = 1
                    else:
                        row_freq_map_dic[board[row][x]] += 1
            row_freq_map_array.append(row_freq_map_dic)

        col_freq_map_array = []
        for col in range(0, len(board)):
            col_freq_map_dic = {}
            for row in range(0, len(board)):
                if board[row][col] != ".":
                    if board[row][col] not in col_freq_map_dic:
                        col_freq_map_dic[board[row][col]] = 1
                    else:
                        col_freq_map_dic[board[row][col]] += 1
            col_freq_map_array.append(col_freq_map_dic)

        box_freq_map = {}
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != ".":
                    box_key = (row//3, col//3)
                    cell = board[row][col]

                    if box_key not in box_freq_map:
                        box_freq_map[box_key] = {}

                    if cell not in box_freq_map[box_key]:
                        box_freq_map[box_key][cell] = 1
                    else:
                        box_freq_map[box_key][cell] += 1

        valid_flag = True
        for x in range(0, len(row_freq_map_array)):
            for key in row_freq_map_array[x]:
                if row_freq_map_array[x][key] > 1:
                    valid_flag = False

        for x in range(0, len(col_freq_map_array)):
            for key in col_freq_map_array[x]:
                if col_freq_map_array[x][key] > 1:
                    valid_flag = False

        for key in box_freq_map:
            for cell in box_freq_map[key]:
                if box_freq_map[key][cell] > 1:
                    valid_flag = False

        return valid_flag

# Every inner array is a row and every index of the inner arrays lined up is a column.
# There are 9 3x3 boxes per "column/row". Meaning, each 3 elements in a row or a column are part of these boxes. Therefore, to find out
# which box we are in, if we take a row and column and divide each of those by 3 (floor division).
# That way, we get 9 unique pairs for boxes (I literally calculated it LMAO). (0,0), (0,1), (0,2) | (1,0), (1,1), (1,2) | (2,0), (2,1), (2,2)
# Next, I had to make frequency maps for all 9 rows, all 9 columns, and all 9 boxes.
# To store the frequency map dictionaries for all 9 rows and 9 columns, I decided to make an array.
# Then I simply looped through the rows and columns, and whatever element was not ".", I made a key, value pair for them. Either
# intialising them or increasing the count if the key for it is already found.
# Took a slightly different approach for boxes. In boxes, I decided to go with dictionary in dictionary approach. For each cell that wasn't
# ".", I floor-divided it's rows and columns by 3. This gave me which "box" it lied in from the 9 boxes. Then I checked if the box_key
# existed in the box frequency map. If it wasn't there, I just initialized a new dictionary for that specific box_key in order to keep track
# of the cell frequency that goes in that particular box. Moving on, I then checked if that cell is particularly found in any box_key's
# frequency map. If it was, then I did the same thing, just add one to it's frequency to find duplicates within the box.
# Then I made a flag and did a check on each one of the frequency maps for all the rows, columns, boxes. If any duplicate was found, we just
# switched the flag.