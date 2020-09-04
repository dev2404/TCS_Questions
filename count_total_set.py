def count_bit(x):
	res = []
	for i in range(x+1):
		count = 0
		while i != 0:
			print(i)
			i = i & (i-1)
			count += 1
		res.append(count)
	return res	

print(count_bit(5))		

