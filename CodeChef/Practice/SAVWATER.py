t = int(input())
for i in range(t):
    H, x, y, C = map(int, input().split())
    ans = x + (y // 2)
    cnt = H * ans
    if cnt <= C:
        print("YES")
    else:
        print("NO")