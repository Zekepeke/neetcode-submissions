class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        seen = set()
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    num_islands += 1
                    queue = deque()

                    cur_row = i
                    cur_col = j

                    queue.append((cur_row, cur_col))

                    while queue:
                        cur_row, cur_col = queue.popleft()
                        for move_rows, move_cols in self.move(grid, cur_row, cur_col):
                            if (move_rows, move_cols) not in seen:
                                seen.add((move_rows, move_cols))
                                queue.append((move_rows, move_cols))

                    
        return num_islands
    
    
                        



    
    # returns an array of where we can move, in cords (row, col)
    def move(self, grid: List[List[str]], cur_row, cur_col) -> List[Tuple[int]]:
        res = []
        bounds_row = len(grid)
        bounds_col = len(grid[0])

        # up
        if cur_row - 1 >= 0 and grid[cur_row - 1][cur_col] == "1":
            res.append((cur_row - 1, cur_col))
        # down
        if cur_row + 1 < bounds_row and grid[cur_row + 1][cur_col] == "1":
            res.append((cur_row + 1, cur_col))
        # left
        if cur_col - 1 >= 0 and grid[cur_row][cur_col - 1] == "1":
            res.append((cur_row, cur_col - 1))
        # right
        if cur_col + 1 < bounds_col and grid[cur_row][cur_col + 1] == "1":
            res.append((cur_row, cur_col + 1))
        return res

        

        