class Solution:
    def __init__(self) -> None:
        self.count = 0

    def search(self, nums: list[int], target: int) -> int:
        half_len = len(nums) // 2

        if(len(nums) > 2):
            while(half_len):
                if(nums[0] < nums[-1]):
                    if(nums[0] <= target < nums[half_len]):
                        return self.search(nums[0:half_len],target)
                    elif(nums[half_len] <= target <= nums[-1]):
                        self.count += half_len
                        return self.search(nums[half_len:],target)
                    else:
                        return -1
                elif(nums[0] > nums[-1]):
                    if((nums[half_len] > nums[-1])):
                        if(nums[0] <= target < nums[half_len]):
                            return self.search(nums[0:half_len],target)
                        else:
                            self.count += half_len
                            return self.search(nums[half_len:],target)
                    elif(nums[half_len] < nums[-1]):
                        if(nums[half_len] <= target <= nums[-1]):
                            self.count += half_len
                            return self.search(nums[half_len:],target)
                        else:
                            return self.search(nums[0:half_len],target)

        if(nums[0] == target):
            return self.count
        elif(nums[-1]==target):
            return self.count + 1
        return -1

test = Solution()
print(test.search(nums = [1,3,5], target = 5))