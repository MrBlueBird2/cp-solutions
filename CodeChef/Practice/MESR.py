t = int(input())
for i in range(t):
    d, n = map(int, input().split())
    print(max(d, n) // min(d, n))