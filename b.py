def decimalbinaryconversion(n):  
    return bin(n).replace("0b", "")  


def length_binary(x, max1):
	x = decimalbinaryconversion(x)
	x_le = len(x)
	max1 = decimalbinaryconversion(max1)
	max1_le = len(max1)
	while (x_le) != (max1_le):
		x = "0" + x
		x_le += 1
	return x	




decimal_number = int(input())
numbers = list(map(int, input().split()))

count = 0
array0 = []
array1 = []

max_of_numbers = max(numbers)
for i in range(decimal_number):
	zeros = length_binary(numbers[i], max_of_numbers).count("0") 
	ones = length_binary(numbers[i], max_of_numbers).count("1")
	array0.append(zeros)
	array1.append(ones)

for i in range(0, decimal_number):
	if array0[i] == array1[i]:
		count += 1
		for j in range(i+1, decimal_number):
			if array0[i] + array0[j] == array1[i] + array1[j]:
				count += 1
				
	
	

	

#print(arr0, arr1)
#print(max1 - len(decimalToBinary(n[0])))
print(length_binary(count, max_of_numbers), end="")
#print(leng(7, 10))