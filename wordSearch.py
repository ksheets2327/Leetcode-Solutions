class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        rows = len(board)
        cols = len(board[0])
        
        path = set()

        def dfs(row, col, index):
            if index == len(word):
                return True
            if (row < 0 or col < 0 or row >= rows or col >= cols or (row, col) in path or board[row][col] != word[index]):
                return False

            path.add((row, col))

            res = (dfs(row - 1, col, index+1) or dfs(row + 1, col, index+1) or dfs(row, col - 1, index+1) or dfs(row, col + 1, index+1))
                    
            path.remove((row,col))

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
            
        return False
 
