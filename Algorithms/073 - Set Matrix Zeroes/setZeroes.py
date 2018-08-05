class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows_to_zero = set()
        cols_to_zero = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows_to_zero.add(row)
                    cols_to_zero.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in rows_to_zero or col in cols_to_zero:
                    matrix[row][col] = 0
