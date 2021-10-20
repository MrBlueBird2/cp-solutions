c, o, r = map(int, input().split())
overs = 20 - o
score = (overs * 6) * 6
ans = r + score
if ans > c:
    print("YES")
else:
    print("NO")