import numpy as np
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        gas_stock = {}
        len_gas = len(gas)
        for i in range(len_gas):
            gas_stock[str(i)] = 0

        for count in range(len_gas):
            key_list = list(gas_stock.keys())
            for index in key_list:
                if(int(index)+count >= len_gas):
                    gas_stock[index] += gas[int(index)+count - len_gas]
                    gas_stock[index] -= cost[int(index)+count - len_gas]
                else:
                    gas_stock[index] += gas[int(index)+count]
                    gas_stock[index] -= cost[int(index)+count]
                if(gas_stock[index] < 0):
                    del gas_stock[index]

        key_list = list(gas_stock.keys())
        if(key_list == []):
            return -1
        else:
            return int(key_list[0])
    
test = Solution()
print(test.canCompleteCircuit([2,3,4], [3,4,3]))