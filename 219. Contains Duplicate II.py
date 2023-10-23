class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        num_dic = {}
        for i, num in enumerate(nums):
            if num in num_dic:
                if i - num_dic[num] <= k:
                    return True
                else:
                    num_dic[num] = i
            else:
                num_dic[num] = i
        return False

test = Solution()
print(test.containsNearbyDuplicate([1,2,3,1], 3))
