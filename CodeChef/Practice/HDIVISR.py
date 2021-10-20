n = int(input())
l = []
for i in range(1, 10+1):
    if n%i == 0:
        l.append(i)
print(max(l))