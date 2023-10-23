class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        nums.sort()

        max_len = 1
        current_index = 0
        dup_num = 0

        if len(nums) == 0:
            return 0
        
        for index in range(1,len(nums)):
            if nums[index] - nums[index-1] == 1:
                if index == len(nums)-1:
                    max_len = max(max_len, index - current_index + 1 - dup_num)
            elif nums[index] - nums[index-1] == 0:
                if index == len(nums)-1:
                    dup_num += 1
                    max_len = max(max_len, index - current_index + 1 - dup_num)
                else:
                    dup_num += 1
            else:
                max_len = max(max_len, index - current_index - dup_num)
                current_index = index
                dup_num = 0
        
        return max_len

test = Solution()
print(test.longestConsecutive([0,0,-1]))
            

            

