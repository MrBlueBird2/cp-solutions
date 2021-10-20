# 25
S = input()
n = int(input())
l = []
for s1 in S:
    for s2 in S:
        l.append(s1+s2)
l.sort()
print(l[n-1])