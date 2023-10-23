import itertools
import numpy as np

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in board:
            check = {}
            for k in i:
                if(k in check.keys()):
                    return False
                elif(k != "."):
                    check[k]=k

        check_arr = np.array(board)
        for i in range(check_arr.shape[1]):
            check = {}
            check_arr2 = check_arr[:, i]
            for k in check_arr2:
                if(k in check.keys()):
                    return False
                elif(k != "."):
                    check[k]=k
        
        check_arr = np.array(board)
        for m in range(3):
            for l in range(3):
                check_arr2 = check_arr[3*m:3*(m+1), 3*l:3*(l+1)]
                check_arr2 = check_arr2.flatten()
                check = {}
                for k in check_arr2:
                    if(k in check.keys()):
                        return False
                    elif(k != "."):
                        check[k]=k
        return True


test = Solution()
print(test.isValidSudoku(board =
[
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".","9","."],
    [".",".",".","5","6",".",".",".","."],
    ["4",".","3",".",".",".",".",".","1"],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]]))
