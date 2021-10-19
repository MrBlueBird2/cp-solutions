# cook your dish here
t = int(input())
for i in range(t):
    g, c = map(int,input().split())
    print((c**2) // (2*g))