a, b, c = map(int,input().split())
ans = a+b
cnt = b+c
mx = a+c
print(max(ans, cnt, mx))