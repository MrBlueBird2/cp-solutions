# cook your dish here
t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    mx = 2 * (180+a)
    mn = b + c
    ans = mx - mn
    print(ans)