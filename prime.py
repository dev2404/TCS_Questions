import math
n = int(input())
k = int(input())
arr = []
c = 0
for i in range(1, int(math.sqrt(n)+1)):
    if n%i == 0:
        arr.append(i)
        arr.append(n//i)
        c += 2
arr.sort()
if c > k:
    print(arr[-k])
    print(arr)
else:
    print(1) 
 

