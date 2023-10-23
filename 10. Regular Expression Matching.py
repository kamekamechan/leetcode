class Solution:
    def str_num(self, s:str):
        output = 1
        for i,x in enumerate(s, start=1):
            if(s[0] == x):
                output = i
            else:
                break
        return output

    def isMatch(self, s: str, p: str) -> bool:
        i, j = 0, 0
        while(j < len(p) and i < len(s)):
            if(p[j] == "."):
                i += 1 
                j += 1
            elif(p[j] == "*"):
                if(p[j-1]=="."):
                    try:
                        temp = i
                        i += self.str_num(s[i:])
                        while(p[j+1]==s[temp]):
                            j += 1
                        j += 1
                    except IndexError:
                        j += 1
                        break
                    except Exception:
                        return False
                elif(p[j-1] == s[i]):
                    try:
                        temp = i
                        i += self.str_num(s[i:])
                        while(p[j+1]==s[temp]):
                            j += 1
                        j += 1
                    except IndexError:
                        j += 1
                        break
                    except Exception:
                        return False
                else:
                    return False
            elif(p[j]==s[i]):
                i += 1
                j += 1
            else:
                try:
                    while(p[j]!=s[i]):
                        j += 1
                except Exception:
                    return False
        if(not ((i==len(s)) and (j==len(p)))):
            return False
        return True

test = Solution()
print(test.isMatch("aaa","ab*a*c*a"))