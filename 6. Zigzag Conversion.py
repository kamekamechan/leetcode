class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output_arr = {}
        output = ""
        for i in range(numRows):
            output_arr[i] = []

        index_arr = self.make_index_arr(len(s), numRows-1)

        for index, string in zip(index_arr, s):
            output_arr[index].append(string)
        
        for key in output_arr.keys():
            output += "".join(output_arr[key])
        
        return output

    def make_index_arr(self, str_len, num):
        if(num == 0):
            return [0] * str_len

        index_arr = []
        count = 0
        increase = True
        while(len(index_arr) < str_len):
            index_arr.append(count)
            if(increase):
                if(count == num):
                    count -= 1
                    increase = False
                else:
                    count += 1
            else:
                if(count == 0):
                    count += 1
                    increase = True
                else:
                    count -= 1
        return index_arr

test= Solution()
print(test.convert("AB", 1))
        



        