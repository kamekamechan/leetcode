class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        original_s_dic = {}
        for index_s, string_s in enumerate(s):
            if(string_s in original_s_dic.keys() and original_s_dic[string_s] == t[index_s]):
                continue
            elif(string_s not in original_s_dic.keys() and t[index_s] not in original_s_dic.values()):
                original_s_dic[string_s] = t[index_s]
            else:
                return False
        return True

test = Solution()
print(test.isIsomorphic("badc","baba"))