from collections import defaultdict
import math
import itertools

class Solution:
    def numDecodings(self, s: str):
        if(s[0] == "0"):
            return 0
        
        div_s_arr = self.div_s(s)
        comb_num_arr = []
        for i in div_s_arr:
            num_count = 0
            for k, str_num in enumerate(self.comb_let(i)):
                plus_num = True
                for m in str_num:
                    if(int(m) == 0 or int(m) > 26):
                        plus_num = False
                        break
                if(plus_num):
                    num_count += 1
            comb_num_arr.append(max(1, num_count))

        answer = 1
        for k in comb_num_arr:
            answer *= k
        return answer

    def div_s (self, s):
        div_s = []
        temp = ""
        for k in s:
            if(k != "0"):
                temp += k
            elif(k == "0"):
                tmp_num = temp[-1]
                div_s.append(temp[:len(temp)-1])
                div_s.append(tmp_num + "0")
                temp = ""
        if(temp):
            div_s.append(temp)
        return div_s

    def comb_let(self, s):
        comb_arr = []
        div_arr = self.make_arr(len(s))
        for arr in div_arr:
            comb_arr.append([])
            count = 0
            for i in arr:
                comb_arr[-1].append(s[count:count+i])
                count += i

        return comb_arr

    def make_arr(self, num):
        output = []
        for i in range(1,num+1):
            if(i==1):
                output.append([1]*num)
            else:
                tmp_num = num
                plus_num = 2
                plus_num_count = 0
                left_num = num - i - plus_num * plus_num_count
                while(plus_num <= i and left_num >= 0):
                    output.append([i] + [plus_num] * plus_num_count + [1] * left_num)
                    if(left_num >= plus_num):
                        plus_num_count += 1
                    else:
                        plus_num += 1
                        plus_num_count = 1
                    left_num = num - i - plus_num * plus_num_count

        tmp_output = []
        for p in output:
            tmp_output.extend(self.shuffle(p))
        return tmp_output

    def all_comb_num(self, arr):
        dic = defaultdict(int)
        for i in arr:
            dic[i] += 1
        under = 1
        for k in dic.values():
            under *= math.factorial(k)
        return int(math.factorial(len(arr))/under)
        

    def shuffle(self, arr):
        output = {}
        dic = {}
        for k in itertools.permutations(arr, len(arr)):
            dic[k] = list(k)

        return list(dic.values())



test = Solution()
# print(test.shuffle([1,1,5]))
print(test.numDecodings(s = "203425225162774522103"))
# print(test.comb_let(s = "226"))
# print(test.make_arr(3))

