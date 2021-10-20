# cook your dish here
t = int(input())
l = []
for i in range(t):
    n = int(input())
    l.append(n)
l.sort()
for i in range(len(l)):
    print(l[i])