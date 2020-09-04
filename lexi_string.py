T = int(input())

while (T > 0):
	P = input()
	S = input()

	list1 = []

	for i in S:
		list1.append(P.find(i))
	list1.sort()

	for i in list1:
		print(P[i], end="")
	if T > 1:
		print()
	T -= 1		

