class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_max_area = 0
        seen = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur_island = 0
                if grid[i][j] == 1 and (i, j) not in seen:
                    seen.add((i, j))
                    queue = deque([(i, j)])
                    while queue:
                        cur_row, cur_col = queue.popleft()
                        cur_island += 1
                        for nr, nc in self.move(grid, cur_row, cur_col):
                            if (nr, nc) not in seen:
                                seen.add((nr, nc))
                                queue.append((nr, nc))
                if cur_island > num_max_area:
                    num_max_area = cur_island


        return num_max_area

    # returns an array of where we can move, in cords (row, col)
    def move(self, grid: List[List[str]], cur_row, cur_col) -> List[Tuple[int]]:
        res = []
        bounds_row = len(grid)
        bounds_col = len(grid[0])

        # up
        if cur_row - 1 >= 0 and grid[cur_row - 1][cur_col] == 1:
            res.append((cur_row - 1, cur_col))
        # down
        if cur_row + 1 < bounds_row and grid[cur_row + 1][cur_col] == 1:
            res.append((cur_row + 1, cur_col))
        # left
        if cur_col - 1 >= 0 and grid[cur_row][cur_col - 1] == 1:
            res.append((cur_row, cur_col - 1))
        # right
        if cur_col + 1 < bounds_col and grid[cur_row][cur_col + 1] == 1:
            res.append((cur_row, cur_col + 1))
        return res
        