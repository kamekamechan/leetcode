from collections import defaultdict

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output_dict = defaultdict(int)

        nums.sort()
        
        left_index, center_index, right_index = 0, 1, len(nums)-1

        while(left_index < center_index < right_index < len(nums)):
            if(nums[left_index] + nums[center_index] + nums[right_index] == 0):
                output_dict[(nums[left_index], nums[center_index], nums[right_index])] = 1
                center_index += 1
                right_index -= 1
            elif(nums[left_index] + nums[center_index] + nums[right_index] < 0):
                center_index += 1
            else:
                right_index -= 1

            if(center_index >= right_index):
                left_index += 1
                center_index = left_index + 1
                right_index = len(nums) - 1

        return [list(taple) for taple in output_dict.keys()]

test = Solution()
print(test.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))