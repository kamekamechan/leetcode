class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_dic = {}
        for char in t:
            if(char in t_dic.keys()):
                t_dic[char] += 1
            else:
                t_dic[char] = 1

        s_dic = {}
        output_string = ""
        for index_s, char in enumerate(s):
            if(char in s_dic.keys()):
                s_dic[char].append(index_s)
            else:
                s_dic[char] = [index_s]

        current_min_index_dic = {}
        for char in t_dic.keys():
            current_min_index_dic[char] = 0

        current_index = len(s)
        for char in t_dic.keys():
            try:
                if(s_dic[char][0] < current_index):
                    current_index = s_dic[char][0]
                    current_char = char
            except Exception:
                return ""
        
        next_index = 0
        next_char = ""
        while(next_index < len(s) or next_index != -1):
            next_index = len(s)
            temp_output_string = ""
            for char in t_dic.keys():
                char_num = t_dic[char]
                if(char == current_char):
                    if(len(s_dic[char]) - current_min_index_dic[char] < char_num):
                        return output_string
                    elif(len(s_dic[char]) - 1 == current_min_index_dic[char]):
                        if(len(temp_output_string) < s_dic[char][current_min_index_dic[char] + char_num -1] - current_index + 1 ):
                            temp_output_string = s[current_index:s_dic[char][current_min_index_dic[char] + char_num -1] + 1]
                        next_index = -1
                    elif(next_index > s_dic[char][current_min_index_dic[char]+1]):
                        next_index = s_dic[char][current_min_index_dic[char]+1]
                        next_char = char
                    if(len(temp_output_string) < s_dic[char][current_min_index_dic[char] + char_num -1] - current_index + 1 ):
                        temp_output_string = s[current_index:s_dic[char][current_min_index_dic[char] + char_num -1] + 1]                            
                    current_min_index_dic[char] += 1
                else:
                    if(len(s_dic[char]) - current_min_index_dic[char] < char_num):
                        return output_string
                    elif(next_index > s_dic[char][current_min_index_dic[char]]):
                        next_index = s_dic[char][current_min_index_dic[char]]
                        next_char = char
                    if(len(temp_output_string) < s_dic[char][current_min_index_dic[char] + char_num -1] - current_index + 1 ):
                        temp_output_string = s[current_index:s_dic[char][current_min_index_dic[char] + char_num -1] + 1]
            
            if(len(output_string) > len(temp_output_string) or output_string == ""):
                output_string = temp_output_string
            current_index = next_index
            current_char  = next_char
            
        return output_string


test =  Solution()
print(test.minWindow("a", "aa"))