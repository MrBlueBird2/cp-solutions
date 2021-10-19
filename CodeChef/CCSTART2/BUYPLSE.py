# cook your dish here
a, b, c, d = map(int,input().split())
ans = min(a, c) * max(a, c) + min(b, d) * max(b, d)
print(ans)