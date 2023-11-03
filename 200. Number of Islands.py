class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_num = 0
        grid_len_x, grid_len_y = len(grid), len(grid[0])
        for index_x in range(grid_len_x):
            for index_y in range(grid_len_y):
                # print(f"{index_x=}, {index_y=}, {grid[index_x][index_y]=}")
                if(grid[index_x][index_y] == "1"):
                    island_num += 1
                    self.paint_out(grid, [index_x, index_y], grid_len_x, grid_len_y)
        return island_num
        
    def paint_out(self, grid, index, grid_len_x, grid_len_y):
        if(0 <= index[0] < grid_len_x and 0 <= index[1] < grid_len_y):
            if(grid[index[0]][index[1]] == "1"):
                grid[index[0]][index[1]] = "0"
                self.paint_out(grid, [index[0]  ,index[1]-1], grid_len_x, grid_len_y)
                self.paint_out(grid, [index[0]-1,index[1]  ], grid_len_x, grid_len_y)
                self.paint_out(grid, [index[0]+1,index[1]  ], grid_len_x, grid_len_y)
                self.paint_out(grid, [index[0]  ,index[1]+1], grid_len_x, grid_len_y)
        