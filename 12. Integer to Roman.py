class Solution:
    def intToRoman(self, num: int) -> str:
        num_to_roman = {"1000":"M", "900":"CM", "500":"D", "400":"CD", "100":"C", "90":"XC",
            "50":"L", "40":"XL","10":"X", "9":"IX", "5":"V", "4":"IV", "1":"I"}

        num_arr = [int(i) for i in num_to_roman.keys()]

        output = ""

        num_for_calc = num
        
        for roman_num in num_arr:
            divide_ans = num_for_calc // roman_num
            num_for_calc = num_for_calc % roman_num

            if(divide_ans != 0):
                output += num_to_roman[str(roman_num)] * divide_ans

        return output

        

test = Solution()
print(test.intToRoman(1994))