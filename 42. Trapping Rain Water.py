class Solution:
    def trap(self, height: list[int]) -> int:
        left_index = 0
        right_index = len(height)-1
        current_height = 1
        max_height = max(height)
        area_sum = 0

        while(left_index <= right_index):
            while(height[left_index] < current_height):
                left_index += 1
            while(height[right_index] < current_height):
                right_index -= 1

            area_sum += right_index - left_index + 1
            if(current_height == max_height):
                break
            else:
                current_height += 1

        return area_sum - sum(height) if area_sum != 0 else 0
    
test = Solution()
print(test.trap([0,2,0]))

