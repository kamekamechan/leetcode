class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for index_s in range(len(s)):
            char_dic = {}
            for index_move in range(len(s)-index_s):
                if(s[index_s + index_move] in char_dic.keys()):
                    max_len = max(max_len, index_move)
                    break
                elif(index_move == len(s) - index_s - 1):
                    max_len = max(max_len, index_move + 1)
                else:
                    char_dic[s[index_s + index_move]] = 1
        
        return max_len

test = Solution()
print(test.lengthOfLongestSubstring("pwwkew"))