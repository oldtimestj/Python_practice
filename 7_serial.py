from random import randint
from itertools import chain

total = []
count = 0

s1 = [randint(60,100) for x in range(39)]
s2 = [randint(60,100) for x in range(45)]
s3 = [randint(60,100) for x in range(51)]
s4 = [randint(60,100) for x in range(40)]

for x in chain(s1,s2,s3,s3):
    if x > 90:
        total.append(x)
        count += 1

print(total)
print(count)