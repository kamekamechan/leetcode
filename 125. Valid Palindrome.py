class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_index = 0
        right_index = len(s)-1

        while(left_index < right_index):

            if(((48 <= ord(s[left_index]) <= 57) or (97 <= ord(s[left_index].lower()) <= 122))
             and ((48 <= ord(s[right_index]) <= 57) or (97 <= ord(s[right_index].lower()) <= 122))):
                if(s[left_index].lower() == s[right_index].lower()):
                    left_index += 1
                    right_index -= 1
                else:
                    return False
            if(ord(s[left_index]) < 48 or 57  < ord(s[left_index].lower()) < 97 or 
                122 < ord(s[left_index].lower())):
                left_index += 1
            elif(ord(s[right_index]) < 48 or 57  < ord(s[right_index].lower()) < 97 or 
                 122 < ord(s[right_index].lower())):
                right_index -= 1
        return True

test =  Solution()
print(test.isPalindrome("ab_a"))