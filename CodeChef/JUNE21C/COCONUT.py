t = int(input())
for i in range(t):
    x, x2, xa, xb = map(int,input().split())
    ans = xa // x
    ans2 = xb // x2
    print(ans+ans2)