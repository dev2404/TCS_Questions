
def mostActive(customers):
    # Write your code here
    length = len(customers)
    arr = set([])
    for i in customers:
        if i not in arr:
            temp = list(customers).count(i)
            if (temp * (100/length)) >= 5:
                arr.add(i)
    return sorted(arr)


print(mostActive["Bigcorp","Bigcorp","Bigcorp","Bigcorp","Bigcorp","Bigcorp","Bigcorp","Bigcorp","Bigcorp","Zork","Zork","Zork","Zork","Zork"])    