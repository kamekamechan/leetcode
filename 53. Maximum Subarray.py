import math

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if(len(nums)==2):
            return max(sum(nums),nums[0],nums[1])
        forward_max_sum = 0
        backward_max_sum = 0
        forward_ind = 0
        backward_ind = -1
        for i in range(math.ceil(len(nums))):
            if(forward_max_sum < 0):
                forward_ind = i
                forward_max_sum = nums[i]
            else:
                forward_max_sum += nums[i]
            
            if(backward_max_sum < 0):
                backward_ind = -(i+1)
                backward_max_sum = nums[-(i+1)]
            else:
                backward_max_sum += nums[-(i+1)]

        backward_ind = len(nums) + backward_ind

        if(forward_ind > backward_ind):
            if(forward_ind == len(nums)-1 and backward_ind ==0):
                return max(nums)
            else:
                return max(sum(nums[forward_ind:]), sum(nums[:backward_ind+1]), nums)
        elif(forward_ind < backward_ind):
            return sum(nums[forward_ind:backward_ind+1], nums)
        else:
            return nums[forward_ind]

test = Solution()
print(test.maxSubArray([-1,-2,-2,-2,3,2,-2,0]))