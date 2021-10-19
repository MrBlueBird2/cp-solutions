# cook your dish here
t = int(input())
for i in range(t):
    d, x, y, z = map(int,input().split())
    mx = x * 7
    mn = y * d + (z * (7 - d))
    print(max(mx, mn))