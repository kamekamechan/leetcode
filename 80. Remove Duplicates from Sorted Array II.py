class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        nums_pointer = 0

        while(nums_pointer < len(nums)-1):
            if(nums[nums_pointer] == nums[nums_pointer + 1]):
                dup_num = 0
                while( ((nums_pointer + dup_num + 1) < len(nums))):
                    if(nums[nums_pointer + dup_num] == nums[nums_pointer + dup_num + 1]):
                        dup_num += 1
                    else:
                        break
                while(dup_num > 1):
                    nums.pop(nums_pointer + dup_num)
                    dup_num -= 1

            nums_pointer += 1

        return len(nums)

test = Solution()
test.removeDuplicates(nums = [0,0,1,1,1,1,2,3,3])