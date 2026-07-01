class Solution:
    def exist(self,board, word):
        rows, cols = len(board), len(board[0])

        def dfs(r, c, index):
        # Base case: matched all letters
            if index == len(word):
                return True

        # Out of bounds or wrong letter or already visited
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False

        # Mark as visited (temporarily)
            temp = board[r][c]
            board[r][c] = "#"

        # Explore all 4 directions
            found = (dfs(r+1, c, index+1) or
                    dfs(r-1, c, index+1) or
                    dfs(r, c+1, index+1) or
                    dfs(r, c-1, index+1))

        # Restore the cell (backtrack)
            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False