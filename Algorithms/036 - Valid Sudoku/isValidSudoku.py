import numpy as np

class Solution:
    def isValidArray(self, arr):
        elements = set()
        for num in arr.flatten():
            if num != '.':
                if num in elements:
                    return False
                elements.add(num)
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        game_board = np.array(board)
        # validate row wise
        for i in range(9):
            if not self.isValidArray(game_board[i]):
                return False

        # validate cols
        for i in range(9):
            if not self.isValidArray(game_board[:,i]):
                return False

        # validate cells
        indicies_to_check = [1, 4, 7]
        for i in indicies_to_check:
            for j in indicies_to_check:
                if not self.isValidArray(game_board[i-1:i+2, j-1:j+2]):
                    return False
        return True

