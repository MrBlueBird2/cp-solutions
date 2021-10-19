# cook your dish here
l, r = map(int,input().split())
for i in range(l, r + 1):
    if i%2 != 0:
        print(i, end=" ")