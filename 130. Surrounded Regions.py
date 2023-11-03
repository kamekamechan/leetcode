class Solution:
    def __init__(self):
        self.checked_index = []

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_len_x, board_len_y = len(board), len(board[0])
        for index_x in range(board_len_x):
            for index_y in range(board_len_y):
                # print(f"{index_x=}, {index_y=}, {grid[index_x][index_y]=}")
                if(board[index_x][index_y] == "O"):
                    self.checked_index = [True]
                    self.paint_out(board, index_x, index_y, board_len_x, board_len_y, self.checked_index)
                    # print(f"{index_x=},{index_y=},{self.checked_index=}")
                    if(self.checked_index.pop(0) is False):
                        for index in self.checked_index:
                            board[index[0]][index[1]] = "O"
        
    def paint_out(self, board, index_x, index_y, board_len_x, board_len_y, checked_index):
        if(checked_index[0] is True):
            if(0 < index_x < board_len_x - 1 and 0 < index_y < board_len_y - 1):
                if(board[index_x][index_y] == "O"):
                    board[index_x][index_y] = "X"
                    checked_index.append([index_x,index_y])
                    self.paint_out(board, index_x  ,index_y-1, board_len_x, board_len_y, checked_index)
                    self.paint_out(board, index_x-1,index_y  , board_len_x, board_len_y, checked_index)
                    self.paint_out(board, index_x+1,index_y  , board_len_x, board_len_y, checked_index)
                    self.paint_out(board, index_x  ,index_y+1, board_len_x, board_len_y, checked_index)
            elif((index_x == 0) or (index_x == board_len_x - 1) or (index_y == 0) or (index_y == board_len_y - 1)):
                if(board[index_x][index_y] == "O"):
                    checked_index[0] = False
        