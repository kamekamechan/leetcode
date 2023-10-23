class Solution:
    def test:
        for a in range(len(a1)):
            for b in range(len(a2)):
                output.append(a1[a]+a2[b])

    def letterCombinations(self, digits: str) -> list[str]:
        digi = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        lett = []
        lett_num = []
        for num in digits:
            lett.append(digi[num])
            lett_num.append(len(digi[num]))

        prod = 1
        for i in lett_num:
            prod *= i

        output = []
        for a in range(len(lett)):
            for b in range(len(lett[a])):
                for i in range(prod//len(lett[a])):
                    try:
                        output[i+((prod//len(lett[a]))-1)*b] += lett[a][b]
                        b += 1
                    except Exception:
                        output.append(lett[a][b])
        return output

test = Solution()
test.letterCombinations("234")






        