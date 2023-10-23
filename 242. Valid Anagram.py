class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for char_s in s:
            if(char_s in s_dict.keys()):
                s_dict[char_s] += 1
            else:
                s_dict[char_s] = 1
        
        for char_t in t:
            if(char_t in s_dict.keys() and s_dict[char_t] > 0):
                s_dict[char_t] -= 1
            else:
                return False
            
        for value in s_dict.values():
            if(value != 0):
                return False
            
        return True
            
test = Solution()
print(test.isAnagram("anagram", "nagaram"))
            