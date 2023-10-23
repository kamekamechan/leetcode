class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if(len(strs)==1):
            return strs[0]

        strs_len_arr = [len(string) for string in strs]

        min_str_index = strs_len_arr.index(min(strs_len_arr))

        min_str = strs[min_str_index]

        matching_str = ""
        for index in range(len(min_str)):
            matching_str = min_str[index]
            for string in strs:
                if(matching_str == string[index]):
                    continue
                else:
                    if(index == 0):
                        return ""
                    else:
                        return min_str[:index]
            if(index == len(min_str)-1):
                return min_str[:index+1]
        return ""


test = Solution()
print(test.longestCommonPrefix(["aab","aa"]))