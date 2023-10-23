from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
class Solution:
    def rotate(self, matrix:list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #辺の長さ6 4 2 7 5 3 1
        #移動量  5 3 1 6 4 2 0
        # i     0 1 2 0 1 2 3  
        #移動回数 4 4 4
        for i in range(int(Decimal(len(matrix)/2).quantize(Decimal('0'), rounding=ROUND_HALF_UP))):
            side_length = len(matrix) - 2*i
            for k in range(side_length-1):
                ind_y = 0
                for m in range(4):
                    move_length = len(matrix) - (1+2*i)
                    if(m==0):
                        temp = matrix[i+ind_y][i+k]
                        while(move_length):
                            if(k+1 < side_length):
                                k += 1
                            else:
                                ind_y += 1
                            move_length -= 1
                    elif(m==1):
                        temp = temp2
                        while(move_length):
                            if(ind_y+1 < side_length):
                                ind_y += 1
                            else:
                                k -= 1
                            move_length -= 1
                    elif(m==2):
                        temp = temp2
                        while(move_length):
                            if(0 <= k-1):
                                k -= 1
                            else:
                                ind_y -= 1
                            move_length -= 1
                    elif(m==3):
                        temp = temp2
                        while(move_length):
                            if(0 <= ind_y-1):
                                ind_y -= 1
                            else:
                                k += 1
                            move_length -= 1

                    temp2 = matrix[i+ind_y][i+k]
                    matrix[i+ind_y][i+k] = temp
                    temp = temp2

# test = Solution()
# test.rotate([[1,2,3],[4,5,6],[7,8,9]])