from random import *
i=0
f1 = open("file1.txt", 'w')
while i < 5:
 print(randint(10000, 100000), file=f1)
 i+=1
f1.close()
ff1 = open("file1.txt", 'r')
f2 = open("result.txt", 'w')
result = 1
for i in ff1:
 i=i.strip()
 x=i
for j in range(len(x)):
 y = int(x[j])
 result = result*y
 print(result, file=f2)

f2.close()
ff1.close()