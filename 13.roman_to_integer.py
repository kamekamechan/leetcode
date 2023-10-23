class Solution:
    def romanToInt(self, s: str) -> int:
        roman_str_num = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        num = 0
        i=0
        while(i<len(s)):
            if (i+1 == len(s)):
                num += roman_str_num[s[i]]
            elif (roman_str_num[s[i]] < roman_str_num[s[i+1]]):
                num += roman_str_num[s[i+1]]-roman_str_num[s[i]]
                i += 1
            else:
                num += roman_str_num[s[i]]
            i += 1
        
        return num

test = Solution()
print(test.romanToInt("III"))