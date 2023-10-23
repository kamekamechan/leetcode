import copy

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        num_dic = {}
        for i in range(len(nums)):
            if(i < len(nums)-1):
                num_dic[str(nums[i])] = nums[i+1]
            elif(i == len(nums) - 1):
                num_dic[str(nums[i])] = None
        
        output = []
        for k in nums:
            output.append([k])

        in_loop = len(nums)
        temp_output = copy.deepcopy(output)
        temp_output2 = []

        while(in_loop):
            for i, let in enumerate(temp_output):
                if(num_dic[str(let[-1])] is None):
                    continue
                else:
                    let.append(num_dic[str(let[-1])])
                    temp_output2.append(let)
            output.extend(temp_output2)
            temp_output = copy.deepcopy(temp_output2)
            temp_output2 = []
            in_loop -= 1

        return output


test = Solution()
print(test.subsets(nums = [1,2,3]))