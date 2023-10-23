class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     output = 0
    #     arr = []        
    #     h_len = len(height)
    #     for i,x in enumerate(height):
    #         if(x*(h_len-i) > output):
    #             for k in range(1,h_len-i):
    #                 # output = max(output, min(x,height[i+k]) * k)
    #                 arr.append(min(x,height[i+k]) * k)
    #     if(len(arr)==0):
    #         return 0
    #     return max(arr)

    def dist(self, i, j):
        if(j < i):
            return j
        else:
            return i

    def maxArea(self, height: list[int]) -> int:
        output = 0
        arr = []        
        h_len = len(height)
        for i in range(len(height)):
            j, k = 0, 0
            while(i-j > 0 or i+k < len(height)):
                output = max(output, min(height[i],height[max(0, i-j)]) * self.dist(i,j),  min(height[i],height[min(i+k, len(height)-1)]) * self.dist(k,len(height)-1-i))
                j += 1
                k += 1
        return output

test = Solution()
print(test.maxArea([1,8,6,2,5,4,8,3,7]))

except Index