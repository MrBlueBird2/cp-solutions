t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    sum = x + y
    print(((6 - sum)/6) if x + y < 6 else 0)