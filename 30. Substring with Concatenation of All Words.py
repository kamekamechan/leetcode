import copy

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_list  = []
        output_arr = []
        word_len = len(words[0])
        words_len = len(words)
        words_dic = {}

        for word in words:
            if(word in words_dic.keys()):
                words_dic[word] += 1
            else:
                words_dic[word] = 1

        index = 0
        while(index < len(s) - word_len * words_len + 1):
            if(s[index:index+word_len] in words and self.check_conformity(s[index:index+word_len*words_len], words_dic, word_len)):
                output_arr.append(index)
            index += 1

        # output_arr = []
        # words_len = len(words)
        # for index in range(0, len(word_list) - words_len + 1):
        #     if(self.check_conformity(word_list[index:index+words_len], copy.deepcopy(words))):
        #         output_arr.append(index * word_len)
                
        return output_arr

    # def check_conformity(self, word_list: list[str], word_list_len,words, word_len) -> bool:
    #     for index in range(0, word_list_len, word_len):
    #         word = word_list[index:index + word_len]
    #         if(word in words):
    #             words.pop(words.index(word))
    #         else:
    #             return False
        
    #     if(words == []):
    #         return True
        
    def check_conformity(self, word_list: list[str], words_dic, word_len) -> bool:
        separated_word_list = []
        for index in range(0, len(word_list), word_len):
            separated_word_list.append(word_list[index:index+word_len])

        for word, count in words_dic.items():
            if(count != separated_word_list.count(word)):
                return False

        return True

test = Solution()
print(test.findSubstring("ababaab", ["ab","ba","ba"]))