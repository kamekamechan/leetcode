class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans

    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     output = 0
    #     if(len(heights) == 1):
    #         return heights[0]

    #     for ind in range(len(heights)):
    #         max_height = heights[ind]
    #         for ind_2 in range(ind + 1, len(heights)):
    #             if(max_height > heights[ind_2]):
    #                 output = max(output, max_height * (ind_2 - ind))
    #                 max_height = heights[ind_2]
    #             elif(max_height <= heights[ind_2]):
    #                 if(max_height == 0):
    #                     break
    #                 elif(ind_2 == len(heights)-1):
    #                     output = max(output, max_height * (ind_2  + 1 - ind))
    #                 else:
    #                     continue
    #     return output

test = Solution()
print(test.largestRectangleArea(height =[2,1,5,6,2,3]))
