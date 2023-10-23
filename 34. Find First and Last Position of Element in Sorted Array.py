class Solution:
    def __init__(self) -> None:
        self.count1 = 0
        self.count2 = 0

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        half_len = len(nums) // 2
        if(len(nums)==1 and nums[0]==target):
            return [0,0]
        elif(len(nums)==2):
            if(nums[0]==target and nums[1]==target):
                return [0,1]
            elif(nums[0]!=target and nums[1]==target):
                return [self.count1 + 1, self.count1 + 1]
            elif(nums[0]==target and nums[1]!=target):
                return [0,0]

        while(len(nums) > 2):
            if(target < nums[half_len]):
                return self.searchRange(nums[0:half_len],target)
            elif(nums[half_len] == target):
                self.count1 += half_len
                self.count2 = self.count1
                j, k = 1,1
                while(0 <= half_len-j):
                    if(nums[half_len-j]!=target):
                        break
                    j += 1
                while(half_len+k < len(nums)):
                    if(nums[half_len+k]!=target):
                        break
                    k += 1
                return [max(0,self.count1-(j-1)),self.count2+(k-1)]
            elif(nums[half_len] < target):
                self.count1 += half_len
                return self.searchRange(nums[half_len:],target)
        return [-1,-1]

test = Solution()
print(test.searchRange(nums = [1,2,2,3,4,4,4], target = 4))