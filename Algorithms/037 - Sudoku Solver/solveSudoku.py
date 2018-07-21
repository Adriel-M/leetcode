class Solution:
    def generatePossibleNumbers(self, board, row, col):
        ret = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        # go through cols for one row
        for i in range(9):
            if i != col:
                ret.discard(board[row][i])

        # go through rows for one col
        for j in range(9):
            if j != row:
                ret.discard(board[j][col])

        # check cell
        # row
        row_min = (row // 3) * 3
        for i in range(row_min, row_min + 3):
            # col
            col_min = (col // 3) * 3
            for j in range(col_min, col_min + 3):
                if i != row and j != col:
                    ret.discard(board[i][j])
        return ret

    def solve(self, board, row, col):
        if row == 9:
            return True
        if board[row][col] == '.':
            possible = self.generatePossibleNumbers(board, row, col)
            if len(possible) == 0:
                return False
            solved = False
            for num in possible:
                board[row][col] = num
                next_row = row + 1 if col == 8 else row
                next_col = 0 if col == 8 else col + 1
                solved = self.solve(board, next_row, next_col)
                if solved:
                    return True
            if not solved:
                board[row][col] = '.'
                return False
        else:
            next_row = row + 1 if col == 8 else row
            next_col = 0 if col == 8 else col + 1
            return self.solve(board, next_row, next_col)

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board, 0, 0)

