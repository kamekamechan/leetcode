class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:

        left_index = 0
        right_index = 1
        output = []

        while(left_index < len(nums) and right_index < len(nums)):

            if(nums[right_index] - nums[right_index - 1] == 0 or nums[right_index] - nums[right_index - 1] == 1):
                right_index += 1
            else:
                if(right_index - 1 == left_index):
                    output.append(str(nums[left_index]))
                else:
                    output.append(str(nums[left_index]) + "->" + str(nums[right_index - 1]))

                left_index = right_index
                right_index += 1

        if(left_index == len(nums)-1):
            output.append(str(nums[left_index]))
            return output
        elif(right_index == len(nums)-1 or right_index == len(nums)):
            output.append(str(nums[left_index]) + "->" + str(nums[-1]))
            return output
    
test = Solution()
print(test.summaryRanges([0,1,2,4,5,7]))
