a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
  if i >= a:
    cnt += 1
print(cnt)