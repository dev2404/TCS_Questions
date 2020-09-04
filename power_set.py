from itertools import combinations

def power_set(x):
	for i in range(0, len(x)+1):
		for element in combinations(x, i):
			print(''.join(element))

power_set(['a','b','c'])	