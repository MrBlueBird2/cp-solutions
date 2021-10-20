# cook your dish here
t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    l = []
    l.append(a)
    l.append(b)
    l.append(c)
    l.sort()
    print(l[1])