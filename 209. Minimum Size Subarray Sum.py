class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        nums.sort()
        left_index = 0
        right_index = len(nums) - 1

        if(nums[-1] >= target):
            return 1

        answer = 0
        while(left_index < right_index):
            if(sum(nums[left_index:right_index + 1]) >= target):
                print(sum(nums[left_index:right_index + 1]))
                answer = right_index - left_index + 1
                left_index += 1
            else:
                if(left_index == 0):
                    return 0
                else:
                    return answer
        return answer
                
    def divide_and_round (self, num1, num2):
        if( (num1 + num2) % 2 == 0):
            return (num1 + num2) // 2
        else:
            return (num1 + num2) // 2 + 1

test = Solution()
print(test.minSubArrayLen(213, [12,28,83,4,25,26,25,2,25,25,25,12]))