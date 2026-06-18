matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

def solution(matrix):
    boundary_top = 0
    boundary_bottom = len(matrix)-1
    boundary_right = len(matrix[0])-1
    boundary_left = 0
    result_array = []

    while boundary_top <= boundary_bottom and boundary_left <= boundary_right:
        for x in range(boundary_left, boundary_right+1):
            result_array.append(matrix[boundary_top][x])

        for x in range(boundary_top+1, boundary_bottom+1):
            result_array.append(matrix[x][boundary_right])

        if boundary_top < boundary_bottom:
            for x in range(boundary_right-1, boundary_left-1, -1):
                result_array.append(matrix[boundary_bottom][x])

        if boundary_left < boundary_right:
            for x in range(boundary_bottom-1, boundary_top, -1):
                result_array.append(matrix[x][boundary_left])

        boundary_top += 1
        boundary_bottom -= 1
        boundary_right -= 1
        boundary_left += 1

    return result_array

# Here's the spiral format:
# 1) The first row entirely except last index.
# 2) Then the last index of all rows.
# 3) Then the last row entirely except last & first index.
# 4) Then the first index of all rows except first row.
# 5) Then the second row entirely except first and last index.
# 6) Then the second last index of all rows except first and last row.
# 7) Then the second last row entirely except last, second last & first, second index.
# 8) Then the second index of all rows except first and last row.
# Then it repeats constantly till the rows merge or whatever.
# Now if we group them:
# 1) The first row entirely except last index.
# 5) Then the second row entirely except first and last index.
# 2) Then the last index of all rows.
# 6) Then the second last index of all rows except first and last row.
# 3) Then the last row entirely except last & first index.
# 7) Then the second last row entirely except last, second last & first, second index.
# 4) Then the first index of all rows except first row.
# 8) Then the second index of all rows except first and last row.
# We need 4 boundary pointers that keep moving inward.
# The top is going to be the first row, the right is going to be the last column.
# The bottom is going to be the last row, the left is going to be the first column.
# We are going to have four for loops that are going to keep adding elements between two distinguished boundaries for each loop.
# The first for loop will be the entire first row, therefore we can say left -> right + 1 (keeping the last element as well)
# The second for loop will be the entire last column except the top-right element (because we already took it in the top row), therefore we
# can say top + 1 (skipping the first element) -> bottom + 1 (keeping the last element)
# The third for loop will be the entire last row except the bottom-right element (because we already took it in the right column), therefore
# we can say right - 1 (skipping the first element) -> left - 1 (keeping the last element), with a step of -1. If we do just left,
# it'll exclude the last element.
# The fourth for loop will be the entire first column except the bottom-left and the top-left elements (because we took bottom-left in the
# last row and top-left in the first row), therefore we can say bottom - 1 (skipping the first element) -> top, with a step of -1. We don't
# need to do top + 1 in this case because then it'll skip the second-last element that we actually need to take, and we also don't do
# top - 1 because we need to skip the last element. Doing top excludes the last element.
# The third and fourth loop we'll only execute if the boundaries of top and bottom and left and right aren't equal to each other. This is
# because if they are equal to each other, then it means there's only a single row/single column remaining, so to avoid duplicates, we don't
# need the entire pass, we just need the initial two for loops of the pass.