
print(True + False)

from collections import defaultdict
d = defaultdict(int)

print(d["test"])
print(d.keys())

print([1]*3)

import numpy as np
test_arr = [1, 2, 3, 4, 5]
print(np.multiply(test_arr, test_arr))
for index, num in enumerate(test_arr, 1):
    print(index, num)

for i in range(-1, -10, -1):
    print(i)

dic = {}
empty = list(dic.keys())
if(empty == []):
    print("hello")

dic = {"1":1, "2":2, "3":3}
print(list(dic.keys()))
for k in list(dic.keys()):
    print(int(k))

num_to_roman = {"1000":"M", "900":"CM", "500":"D", "400":"CD", "100":"C", "90":"XC",
            "50":"L", "40":"XL","10":"X", "9":"IX", "5":"V", "4":"IV", "1":"I"}

num_arr = [int(i) for i in num_to_roman.keys()]
print(num_arr)

test_string = "testdesu"
print(test_string[:0])

test = {("1,2,3"):[1,2,3]}

dic_1 = {"a":2, "n":4, "b":5}
print(tuple(sorted(list(dic_1.items()))))

arr = [1,2,3,4,5,6,7,8]
print(arr[-4:-2])

points = [[2,16],[2,8],[1,6],[7,12]]
points.sort(key=lambda x: x[0], reverse=True)
print(points)

dic = {1:"orange",3:"lemon", 2:"suika"}
print(dic)
dic = dict(sorted(dic.items()))
print(dic)

test_array = [2]
test_array.sort()
print(test_array)

print(1*bool(None))

a, b = 1, 4
a, b = b, a
print(f"{a}, {b}")

test = [1,2,3,4,5]
print(test[4:-1])
if([]):
    print("[]=true")



