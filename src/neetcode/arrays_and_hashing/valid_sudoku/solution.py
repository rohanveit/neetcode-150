class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()
        # horizontal
        for row_idx, row in enumerate(board):
            for column_idx, number in enumerate(row):
                # disregard 'empty' squares
                if number == '.':
                    continue

                msg1 = f"{number} seen in row {row_idx}"
                msg2 = f"{number} seen in column {column_idx}"
                msg3 = f"{number} seen in sub-square ({row_idx // 3},{column_idx // 3})"
                all_msgs = [msg1, msg2, msg3]

                if any(msg in seen for msg in all_msgs):
                    return False
                seen.update(all_msgs)

        return True
