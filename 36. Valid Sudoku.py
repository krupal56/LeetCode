class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowHash = defaultdict(set)
        columnHash = defaultdict(set)
        gridHash = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rowHash[i] or
                    board[i][j] in columnHash[j] or
                    board[i][j] in gridHash[(i // 3,j // 3)]):
                    return False
                rowHash[i].add(board[i][j])
                columnHash[j].add(board[i][j])
                gridHash[(i//3,j//3)].add(board[i][j])
        return True  