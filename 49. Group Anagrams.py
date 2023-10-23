class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs_dic_with_len = {}

        for str in strs:
            str_dic, str_len = self.return_str_dic(str)
            if(str_len in strs_dic_with_len.keys()):
                dic_index = tuple(sorted(list(str_dic.items())))
                if(dic_index in strs_dic_with_len[str_len].keys()):
                    strs_dic_with_len[str_len][dic_index].append(str)
                else:
                    strs_dic_with_len[str_len][dic_index] = [str]
            else:
                strs_dic_with_len[str_len] = {tuple(sorted(list(str_dic.items()))):[str]}

        output = []
        for str_len in strs_dic_with_len.keys():
            for dic_index in strs_dic_with_len[str_len].keys():
                output.append(strs_dic_with_len[str_len][dic_index])

        return output

    def return_str_dic(self, strs):
        strs_dic = {}
        strs_len = len(strs)

        for char in strs:
            if char not in strs_dic:
                strs_dic[char] = 1
            else:
                strs_dic[char] += 1

        return [strs_dic, strs_len]
    
test = Solution()
print(test.groupAnagrams(["ddddddddddg","dgggggggggg"]))