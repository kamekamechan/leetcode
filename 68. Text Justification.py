class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        output_arr = []

        len_count = 0
        input_word_arr = []
        while(words != []):
            word = words.pop(0)
            if(words != []):
                if(len_count + len(word) + len(input_word_arr) > maxWidth):
                    output_arr.append(self.locate_words(input_word_arr, maxWidth, False))
                    input_word_arr = []
                    len_count = 0
            else:
                if(len_count + len(word) + len(input_word_arr) > maxWidth):
                    output_arr.append(self.locate_words(input_word_arr, maxWidth, False))
                    output_arr.append(self.locate_words([word], maxWidth, True))
                else:
                    input_word_arr.append(word)
                    output_arr.append(self.locate_words(input_word_arr, maxWidth, True))
                input_word_arr = []
                len_count = 0
            
            input_word_arr.append(word)
            len_count += len(word)
            print(words)
        return output_arr

    def locate_words(self, word_arr, maxWidth, last_words):
        word_num = len(word_arr)
        output_string = ""

        if(last_words or len(word_arr) == 1):
            for word in word_arr:
                output_string += word + " "
            output_string += " " * (maxWidth - len(output_string))
        else:
            sum_word_len = 0
            for word in word_arr:
                sum_word_len += len(word)
            
            space_num = maxWidth - sum_word_len
            space_arr = [space_num // (word_num - 1)] * (word_num - 1)
            for i in range(space_num % (word_num - 1)):
                space_arr[i] += 1
            space_arr.append(0)

            for word, space_num in zip(word_arr, space_arr):
                output_string += word + " " * space_num
        
        return output_string

test = Solution()
print(test.locate_words(["Science","is","what","we"], 20, False))
print(test.fullJustify(
["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
, 16))

test = "test "
print(test)

import datetime
dt_now = datetime.datetime.now()
print(dt_now.strftime('%Y-%m-%d-%H-%M'))
