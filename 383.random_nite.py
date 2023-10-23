class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        try:
            for i,x in enumerate(ransomNote):
                magazine.pop(magazine.index(x))
        except Exception:
            return False
        return True
    

a = Solution()
print(a.canConstruct("aa","aab"))
