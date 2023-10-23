class Solution:
    def hIndex(self, citations: list[int]) -> int:
        temp_list = sorted(citations)

        return_value = 0
        len_list = len(citations)
        for index, num in enumerate(temp_list):
            if( num  - (len_list-index) <= 0):
                return_valaue = num

        return return_value
    
temp = Solution()
print(temp.hIndex([3,0,6,1,5])) # 3