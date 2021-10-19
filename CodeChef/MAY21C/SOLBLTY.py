# cook your dish here
t = int(input())
for i in range(t):
    x, a, b = map(int,input().split())
    ans = (a + (100 - x) * b) * 10
    print(ans)