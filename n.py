n = int(input())

b, h = input().split(' ')

l = [int(j) for j in input().split()]
l.append(0)

t = [-1]
a = 0
s = 0


for i in range(0, n):
    s += l[i]*int(h)*int(b)

    while l[t[-1]] > l[i]:
        m = l[t.pop()]
        n = i - t[-1] - 1
        a = max(m * n, a)

    t.append(i)
l.pop()

print(abs(a * int(h) * int(b) - int(s))%((10**9)+7),end='')


