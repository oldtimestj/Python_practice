from random import randint
from itertools import chain

total = []
chinses = [randint(60,100) for x in range(40)]
math = [randint(60,100) for x in range(40)]
english = [randint(60,100) for x in range(40)]

for c,m,e in zip(chinses,math,english):
    total.append(c+m+e)
print(total)