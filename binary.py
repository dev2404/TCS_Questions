def decimalToBinary(n):  
    return bin(n).replace("0b", "")  


def leng(x, max1):
	x = decimalToBinary(x)
	x_le = len(x)
	max1 = decimalToBinary(max1)
	max1_le = len(max1)
	while (x_le) != (max1_le):
		x = "0" + x
		x_le += 1
	return x	




x = int(input())
n = list(map(int, input().split()))

c = 0
arr0 = []
arr1 = []

max1 = max(n)
for i in range(x):
	zeros = leng(n[i], max1).count("0") 
	ones = leng(n[i], max1).count("1")
	arr0.append(zeros)
	arr1.append(ones)

for i in range(1, x):
	if arr0[i-1] + arr1[i-1] == arr0[i] + arr1[i]:
		c += 1
	if arr0[i] == arr1[i]:
		c += 1
	

	

print(arr0, arr1)
#print(max1 - len(decimalToBinary(n[0])))
print(leng(c, max1))
#print(leng(7, 10))