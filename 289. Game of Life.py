import copy
class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_copy = copy.deepcopy(board)
        for row_index in range(len(board)):
            for column_index in range(len(board[0])):
                lives_count = self.count_around_lives([row_index, column_index], board_copy)
                if(lives_count <= 1 or lives_count >= 4):
                    board[row_index][column_index] = 0
                elif(lives_count == 3):
                    board[row_index][column_index] = 1

        return board

    def count_around_lives(self, current_index, board):
        current_index_x, current_index_y = current_index
        row_num = len(board)
        column_num = len(board[0])

        search_index_x, search_index_y = current_index_x, current_index_y
        offset_index = [[-1, -1], [0, -1], [1, -1],[-1, 0], [1, 0],[-1, 1], [0, 1], [1, 1]]
        lives_count = 0
        while(offset_index != []):
            offset = offset_index.pop()
            if(0 <= current_index_x + offset[0] < row_num and 0 <= current_index_y + offset[1] < column_num and board[current_index_x + offset[0]][current_index_y + offset[1]] == 1):
                lives_count += 1

        return lives_count

test = Solution()
print(test.gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))


        