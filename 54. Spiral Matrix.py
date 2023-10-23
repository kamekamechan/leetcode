import numpy as np

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        matrix = np.array(matrix)

        if(matrix.shape[0] == 0 or matrix.shape[1] == 0):
            return ""
        elif(matrix.shape[0] == 1):
            return matrix[0]
        elif(matrix.shape[1] == 1):
            return matrix[:,0]
        
        output = []

        ind_x = 0
        ind_y = 0
        while(ind_y < matrix.shape[1]):
            output.append(matrix[ind_x, ind_y])
            ind_y += 1
        ind_x += 1
        ind_y -= 1

        while(ind_x < matrix.shape[0] and ind_y == matrix.shape[1]-1):
            output.append(matrix[ind_x, ind_y])
            ind_x += 1
        ind_x -= 1
        ind_y -= 1

        while(ind_x == matrix.shape[0]-1 and 0 <= ind_y):
            output.append(matrix[ind_x, ind_y])
            ind_y -= 1
        ind_x -= 1
        ind_y += 1

        while(1 <= ind_x and ind_y == 0):
            output.append(matrix[ind_x, ind_y])
            ind_x -= 1
        ind_x += 1

        output.extend(self.spiralOrder(matrix[1:matrix.shape[0]-1, 1:matrix.shape[1]-1]))

        return output

test = Solution()
print(test.spiralOrder([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]))