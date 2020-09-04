num = int(input("enter the integer:"))
num1 = int(input("enter the divisor:"))
count = 0
while num >= num1:
	num = num - num1
	count += 1

if num > 1:
	print("REMAINDER:QUOTIENT",num,count)
else:
	print(count)

	

