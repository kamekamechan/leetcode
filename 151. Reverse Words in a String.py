class Solution:
    def reverseWords(self, s: str) -> str:
        word_arr = self.sep_sentence(s)

    def sep_sentence(self, s:str) -> str:
        if(s == ""):
            return []
        elif(len(s) == 1):
            return [s]
        
        left_index = 0
        
        word_arr = []
        while(left_index  < len(s) - 1):
            while(s[left_index] == " "):
                if(left_index < len(s) - 1):
                    left_index += 1
                else:
                    return word_arr

            if(left_index == len(s)-1):
                word_arr.append(s[left_index])
                return word_arr

            right_index = left_index + 1

            while(s[right_index] != " "):
                if(right_index < len(s) - 1):
                    right_index += 1
                else:
                    word_arr.append(s[left_index:right_index+1])
                    return word_arr

            word_arr.append(s[left_index:right_index])
            left_index = right_index
        return word_arr

test = Solution()
print(test.sep_sentence("b"))