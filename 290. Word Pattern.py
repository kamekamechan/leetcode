class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if(len(pattern) != len(s.split())):
            return False

        pattern_dic = {}
        for index_s, string_s in enumerate(s.split()):
            if(pattern[index_s] in pattern_dic.keys() and pattern_dic[pattern[index_s]] == string_s):
                continue
            elif(pattern[index_s] not in pattern_dic.keys() and string_s not in pattern_dic.values()):
                pattern_dic[pattern[index_s]] = string_s
            else:
                return False
        return True
    
test =  Solution()
print(test.wordPattern("jquery", "jquery"))
