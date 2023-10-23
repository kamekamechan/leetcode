import copy

class Solution:
    def __init__(self):
        self.x_ind = 0
        self.y_ind = 0
        self.ind = 0

    def exist(self, board: list[list[str]], word: str) -> bool:

        while(self.x_ind < len(board)):
            if(self.ind == 0):
                if(board[self.x_ind][self.y_ind] == word[self.ind]):
                    temp_board = copy.deepcopy(board)
                    temp_board[self.x_ind][self.y_ind] = None
                    self.ind += 1
                else:
                    self.add(board)
            else:
                if(self.area_scan(copy.deepcopy(temp_board), word[self.ind], self.x_ind, self.y_ind) == []):
                    self.ind = 0
                    self.add(board)
                else:
                    if(self.bool_match(copy.deepcopy(temp_board), word, self.x_ind, self.y_ind)):
                        return True
                    else:
                        self.ind = 0
                        self.add(board)
                        continue
        return False

    def area_scan(self, board, string, x_ind, y_ind):
        match_arr = []
        for i, m in zip([-1, 0, 0, 1], [0, -1, 1, 0]):
            x, y = x_ind + i, y_ind + m
            if(x < 0 or x > (len(board)-1)):
                continue
            elif(y < 0 or y > (len(board[0])-1)):
                continue
            elif(board[x][y] == string):
                match_arr.append([x,y])
                board[x_ind][y_ind] = None
        return match_arr

    def bool_match(self, board, word, x_ind, y_ind):
        temp_ind = self.ind
        for k in self.area_scan(board, word[self.ind], x_ind, y_ind):
            self.ind += 1
            if(self.ind >= len(word)):
                return True
            elif(self.bool_match(copy.deepcopy(board), word, k[0], k[1])):
                return True
            else:
                self.ind = temp_ind
        return False
    
    def add(self, board):
        if(self.y_ind < len(board[0])-1):
            self.y_ind += 1
        else:
            self.x_ind += 1
            self.y_ind = 0

test = Solution()
print(test.exist(board =
[["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], word =
"AAAAAAAAAAAAAAB"))