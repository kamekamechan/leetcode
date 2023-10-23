# class Solution:
#     def cov_num(self, s:str, t:str) -> int:
#         count = 0
#         for i in s:
#             if(i == t):
#                 count += 1
#             else:
#                 break
#         return count

#     def isMatch(self, s: str, p: str) -> bool:
#         if(len(p)==0):
#             if(len(s)==0):
#                 return True
#             return False

#         elif(len(s)==0):
#             for i in range(len(p)):
#                 if(p[i] != "*"):
#                     return False
#             return True
        
#         for i in range(len(p)):
#             if(p[i] != "*"):
#                 break
#             elif(i==len(p)-1):
#                 return True

#         if(p[0]=="?"):
#             return self.isMatch(s[self.cov_num(p,"?"):],p[self.cov_num(p,"?"):])
#         elif(p[0]=="*"):
#             if(len(p)==1):
#                 return True
#             else:
#                 for i in range(len(s)):
#                     if(self.isMatch(s[i:],p[self.cov_num(p,"*"):])):
#                         return True
#                 return False
#         else:
#             if(p[0] == s[0]):
#                 step = min(self.cov_num(p,p[0]),self.cov_num(s,p[0]))
#                 return self.isMatch(s[step:],p[step:])
#             else:
#                 return False
#         return False


class Solution:
    def __init__(self):
        self.there_ast = False

    def cov_num(self, s:str, t:str) -> int:
        count = 0
        for i in s:
            if(i == t):
                count += 1
            else:
                break
        return count

    def distin_match(self, s: str, p:str) -> bool:
        for k in range(len(s)):
            for i in range(len(p)):
                if(k+i >= len(s)):
                    return False,0
                elif(p[i] != "?" and p[i] != s[k+i]):
                    break
                elif(i == len(p)-1):
                    if(k == 0 or self.there_ast):
                        return True, k+i+1
                    return False, 0
                else:
                    continue
        return False,0

    def isMatch(self, s: str, p: str) -> bool:
        for i in range(len(p)):
            if(p[i] != "*"):
                break
            elif(i==len(p)-1):
                return True

        while(len(s) and len(p)):
            ind_s, ind_p = 0, 0
            if(p[ind_p]!="*"):
                while(ind_p < len(p)):
                    if(p[ind_p]!="*"):
                        ind_p += 1
                test = self.distin_match(s,p[:ind_p])
                if(test[0]):
                    s = s[test[1]:]
                    p = p[ind_p:]
                    if(len(p) == 0 and self.there_ast):
                        return True
                else:
                    return False
                self.there_ast = False
            else:
                for i in range(len(p)):
                    if(p[i] != "*"):
                        break
                    elif(i==len(p)-1):
                        return True
                p = p[self.cov_num(p,"*"):]
                self.there_ast = True
        
        if(len(p)==0):
            if(len(s)==0):
                return True
            return False

        elif(len(s)==0):
            for i in range(len(p)):
                if(p[i] != "*"):
                    return False
            return True

test = Solution()
print(test.isMatch("cb","***a"))