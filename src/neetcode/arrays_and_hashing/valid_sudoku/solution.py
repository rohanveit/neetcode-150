class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()
        # horizontal
        for row in board:
            seen = set()
            for num in row:
                if num not in seen:
                    seen.add(num)
                elif num != '.':
                    return False

        seen = set()
        for i in range(len(board)):
            seen = set()
            for row in board:
                if row[i] not in seen:
                    seen.add(num)
                elif num != '.':
                    return False

        for i in range(0, len(board), 3):
            pass
