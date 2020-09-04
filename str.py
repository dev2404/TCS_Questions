def reverse(string, low, way, array):
	if low == len(string):
		if len(way) ==3:
			array.append(way)
		return
	for end in range(low + 1, len(string) + 1):
		sub = string[low: end]
		if sub == sub[::-1]:
			reverse(string, end, way + [sub], array)

def palindrome_string(string): 
	array = []
	reverse(string, low=0, way=[], array=array)	
	return array	


string = input()
if len(string+1)%3 != 0:
	print("Impossible")

else:	
	arr = [] 
	arr = (palindrome_string(string))
	for i in arr[0]:
		print(i)
