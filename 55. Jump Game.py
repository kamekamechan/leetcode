class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if(len(nums)==1):
            return True
        elif(nums[0]==0):
            return False

        # for num_of_step in nums:
        can_or_not = False
        num_of_step = nums[0]
        for steps_to_go in range(num_of_step):
            can_or_not = can_or_not or self.canJump(nums[steps_to_go + 1:])
        
        return can_or_not
            
test = Solution()
print(test.canJump([2,3,1,1,4])) # False