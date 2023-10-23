class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        output = []

        left_index = 0
        left_array = intervals[left_index]
        right_index = 1

        while(left_index < len(intervals) and right_index < len(intervals)):
            if left_array[1] >= intervals[right_index][0]:
                left_array = [min(left_array[0], intervals[right_index][0]), max(left_array[1], intervals[right_index][1])]
                right_index += 1
            else:
                output.append(left_array)
                left_index = right_index
                left_array = intervals[left_index]
                right_index += 1

        if(left_index == len(intervals) - 1):
            output.append(left_array)
        else:
            output.append([left_array[0], max(left_array[1], intervals[-1][1])])
        
        return output
    
test = Solution()
print(test.merge([[1,4],[0,1]]))