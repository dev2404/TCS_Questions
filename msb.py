import math

def msb(n): 
	c = 0
	#k = int(math.log(n, 2))
	#return 2 ** k
	while n > 0:
		c += 1
		n = n>>1
	return c	
    
	
print(msb(16))
